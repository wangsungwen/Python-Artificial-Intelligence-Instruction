# 語音 AI 與多語字幕影片：技術教學補充教材

本教材適用具 Python 基礎的資工系學生，延伸第 4 週語音 AI 與影片生成課程。技術資料查核日期：2026-11-03。

## 教材下載

- [49 頁教學簡報（PPTX，含逐頁講者備註）](語音AI與多語字幕影片_技術教學簡報.pptx)
- [逐頁詳細講義（HTML，含簡報畫面與來源）](語音AI與多語字幕影片_逐頁教學講義.html)
- [完整教材包（ZIP）](語音AI與多語字幕影片_完整技術教材.zip)
- [開始使用與實作說明](開始使用與實作說明.txt)

HTML 請下載後用瀏覽器開啟，GitHub 檔案頁不會直接執行或呈現完整 HTML 網頁。內嵌圖片可離線閱讀，也可用瀏覽器列印成 PDF。

## 學習內容

語音合成技術演進、開源模型選型、多語翻譯、ASR 與字幕對齊、V1／V2 函式與資料流、影片時間軸、字幕軌與燒錄、部署與測試。

本教材將既有實作與延伸設計分開說明。V2 原始輸出為影片與獨立 SRT；新增工具可將字幕封裝成可切換軌道，或直接燒錄到畫面。

## 字幕實作

需要 Python 3.10+，以及 PATH 中可執行的 FFmpeg／ffprobe。燒錄需 subtitles/libass 濾鏡、libx264 與中文字型。字幕工具本身不需第三方 Python 套件，也不需 GPU。

```shell
python subtitle_tools.py srt cues.example.json demo.srt
python subtitle_tools.py soft video.mp4 subtitles.srt video_soft.mp4 --language zho
python subtitle_tools.py burn video.mp4 subtitles.srt video_burn.mp4
python -m unittest test_subtitle_tools.py -v
```

- [字幕工具](subtitle_tools.py)
- [雙語字幕時間示例](cues.example.json)
- [單元測試](test_subtitle_tools.py)

工具不會執行語音辨識或翻譯，不覆蓋原檔或既有輸出。詳細限制與字型設定見操作說明。

## 驗證範圍

6 個單元測試已通過；已用 3 秒測試影片驗證字幕軌封裝、中英字幕燒錄及輸出時長。本次未重新執行 TTS、ASR 或翻譯模型的 GPU 端到端測試。

模型權重、程式、字型與輸入素材各有自己的授權；來源與條款摘要見簡報及逐頁講義。
