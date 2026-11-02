"""Teaching utility: JSON cues to SRT, MP4 soft subtitles, and burn-in.

Python 3.10+. Requires FFmpeg and ffprobe on PATH for media operations.
Never overwrites inputs or existing outputs. Does not run ASR or translation.
"""
import argparse
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path


def milliseconds(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError('Time must be a number, not bool.')
    if not math.isfinite(value) or value < 0:
        raise ValueError('Time must be finite and nonnegative.')
    return round(value * 1000)


def timestamp(ms):
    hours, ms = divmod(ms, 3600000)
    minutes, ms = divmod(ms, 60000)
    seconds, ms = divmod(ms, 1000)
    return f'{hours:02}:{minutes:02}:{seconds:02},{ms:03}'


def cues_to_srt(cues):
    if not isinstance(cues, list) or not cues:
        raise ValueError('Expected a nonempty list of cues.')
    records, previous_end = [], 0
    for index, cue in enumerate(cues, 1):
        if not isinstance(cue, dict) or not {'start', 'end', 'text'} <= cue.keys():
            raise ValueError(f'Cue {index}: missing start/end/text.')
        start, end = milliseconds(cue['start']), milliseconds(cue['end'])
        if end <= start or start < previous_end:
            raise ValueError(f'Cue {index}: zero duration, overlap or wrong order.')
        if not isinstance(cue['text'], str) or not cue['text'].strip():
            raise ValueError(f'Cue {index}: empty text.')
        text = '\n'.join(x.strip() for x in cue['text'].splitlines() if x.strip())
        if '\x00' in text or '-->' in text:
            raise ValueError(f'Cue {index}: unsupported control text.')
        records.append(f'{index}\n{timestamp(start)} --> {timestamp(end)}\n{text}\n')
        previous_end = end
    return '\n'.join(records)


def new_output(path, inputs=()):
    path = Path(path).resolve()
    if path in [Path(p).resolve() for p in inputs] or path.exists():
        raise FileExistsError(f'Choose a new output filename: {path}')
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def run(args, cwd=None):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                            encoding='utf-8', errors='replace', timeout=1800)
    if result.returncode:
        raise RuntimeError(result.stderr[-5000:])
    return result.stdout


def media(video, subtitle, output, mode, language='und', fonts=None):
    ffmpeg, ffprobe = shutil.which('ffmpeg'), shutil.which('ffprobe')
    if not ffmpeg or not ffprobe:
        raise RuntimeError('Install FFmpeg and ffprobe, and add them to PATH.')
    video, subtitle = Path(video).resolve(), Path(subtitle).resolve()
    if not video.is_file() or not subtitle.is_file():
        raise FileNotFoundError('Video or SRT does not exist.')
    if video.suffix.lower() != '.mp4' or subtitle.suffix.lower() != '.srt':
        raise ValueError('This teaching utility accepts MP4 and SRT inputs.')
    out = new_output(output, (video, subtitle))
    if out.suffix.lower() != '.mp4':
        raise ValueError('Output must use .mp4.')
    subtitle_text = subtitle.read_text(encoding='utf-8-sig')
    if not subtitle_text.strip():
        raise ValueError('SRT is empty.')
    # Probe is an integration check, not a full audit of arbitrary external SRT.
    meta = json.loads(run([ffprobe, '-v', 'error', '-show_streams', '-of', 'json', str(video)]))
    if not any(s['codec_type'] == 'video' for s in meta['streams']):
        raise ValueError('Input has no video stream.')
    with tempfile.TemporaryDirectory(prefix='subtitle_lab_') as tmp:
        work = Path(tmp)
        (work / 'subtitles.srt').write_text(subtitle_text, encoding='utf-8')
        args = [ffmpeg, '-hide_banner', '-loglevel', 'error', '-nostdin', '-n', '-i', str(video)]
        if mode == 'soft':
            args += ['-i', 'subtitles.srt', '-map', '0:v:0', '-map', '0:a?', '-map', '1:0',
                     '-c:v', 'copy', '-c:a', 'copy', '-c:s', 'mov_text',
                     '-metadata:s:s:0', f'language={language}', '-disposition:s:0', 'default']
        elif mode == 'burn':
            filters = run([ffmpeg, '-hide_banner', '-filters'])
            if not any('subtitles' in line.split() for line in filters.splitlines()):
                raise RuntimeError('This FFmpeg build has no subtitles/libass filter.')
            vf = 'subtitles=subtitles.srt'
            if fonts:
                fonts = Path(fonts).resolve()
                if not fonts.is_dir():
                    raise ValueError('--fonts must be a directory of font files.')
                font_files = [f for f in fonts.iterdir() if f.suffix.lower() in {'.ttf', '.otf', '.ttc'}]
                if not font_files:
                    raise ValueError('No TTF/OTF/TTC font files found.')
                (work / 'fonts').mkdir()
                for f in font_files:
                    shutil.copy2(f, work / 'fonts' / f.name)
                vf += ':fontsdir=fonts'
            args += ['-map', '0:v:0', '-map', '0:a?', '-vf', vf, '-c:v', 'libx264',
                     '-crf', '20', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy']
        else:
            raise ValueError('Mode must be soft or burn.')
        args += ['-movflags', '+faststart', str(out)]
        run(args, cwd=work)
    result = json.loads(run([ffprobe, '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(out)]))
    if mode == 'soft' and not any(s['codec_type'] == 'subtitle' for s in result['streams']):
        raise RuntimeError('Output has no subtitle stream.')
    return out, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    srt = sub.add_parser('srt', help='Convert validated JSON cues to UTF-8 SRT.')
    srt.add_argument('cues'); srt.add_argument('output')
    for kind in ('soft', 'burn'):
        p = sub.add_parser(kind)
        p.add_argument('video'); p.add_argument('subtitle'); p.add_argument('output')
        if kind == 'soft':
            p.add_argument('--language', default='und', help='Subtitle language tag, e.g. eng or zho.')
        else:
            p.add_argument('--fonts', help='Directory with licensed Chinese-capable TTF/OTF/TTC fonts.')
    args = parser.parse_args()
    if args.command == 'srt':
        data = json.loads(Path(args.cues).read_text(encoding='utf-8-sig'))
        text = cues_to_srt(data)
        dest = new_output(args.output, (args.cues,))
        with dest.open('x', encoding='utf-8') as handle:
            handle.write(text)
        print(dest)
    else:
        dest, result = media(args.video, args.subtitle, args.output, args.command,
                             getattr(args, 'language', 'und'), getattr(args, 'fonts', None))
        print(json.dumps({'output': str(dest), 'streams': [s['codec_type'] for s in result['streams']],
                          'duration': result['format'].get('duration')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
