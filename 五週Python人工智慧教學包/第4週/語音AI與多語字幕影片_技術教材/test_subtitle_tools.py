import tempfile
import unittest
from pathlib import Path
from subtitle_tools import cues_to_srt, milliseconds, timestamp, new_output


class SubtitleTests(unittest.TestCase):
    def test_rounding_carries_to_minute(self):
        self.assertEqual(timestamp(milliseconds(59.9996)), '00:01:00,000')

    def test_invalid_times(self):
        for value in (True, -1, float('nan'), float('inf'), '1'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                milliseconds(value)

    def test_millisecond_collapse(self):
        with self.assertRaises(ValueError):
            cues_to_srt([{'start': 1, 'end': 1.0001, 'text': 'x'}])

    def test_overlap(self):
        with self.assertRaises(ValueError):
            cues_to_srt([{'start': 0, 'end': 2, 'text': 'a'}, {'start': 1, 'end': 3, 'text': 'b'}])

    def test_bilingual_and_contiguous(self):
        output = cues_to_srt([{'start': 0, 'end': 1, 'text': '你好\nHello'},
                             {'start': 1, 'end': 2, 'text': '再見'}])
        self.assertIn('你好\nHello', output)
        self.assertIn('2\n00:00:01,000 --> 00:00:02,000', output)

    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'existing.srt'
            path.write_text('keep')
            with self.assertRaises(FileExistsError):
                new_output(path)
            self.assertEqual(path.read_text(), 'keep')


if __name__ == '__main__':
    unittest.main()
