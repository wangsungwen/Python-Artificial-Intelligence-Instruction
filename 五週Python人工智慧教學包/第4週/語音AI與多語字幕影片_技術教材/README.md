# 語音 AI 與多語字幕影片：技術教學補充教材

本教材適用具 Python 基礎的資工系學生，延伸第 4 週語音 AI 與影片生成課程。技術資料查核日期：2026-11-03。

## 建議閱讀順序

1. **先看一個場景怎麼變成影片。** 用 [49 頁技術簡報](語音AI與多語字幕影片_技術教學簡報.pptx) 建立全貌，沿著「圖片與台詞 → 翻譯 → 各語言旁白 → 字幕與影片」追蹤資料。課後可用 [逐頁圖文講義](語音AI與多語字幕影片_逐頁教學講義.html) 對照投影片與技術來源。
2. **再對照新版原始碼。** [Word 逐行講義（37 頁）](F5雙引擎與字幕開關_原始程式逐行講義.docx) 適合列印與課堂共讀。34 個段落各處理一個邏輯，逐行說明 246 行精選原始碼。先找出純語音版第 8B 格寫出 WAV 的位置，再看影片版如何透過 `F5Adapter` 產生各場景旁白。閱讀時可圈出 `ref_text`（參考錄音的逐字稿）和 `gen_text`（要合成的台詞），追蹤兩者分別傳給哪個參數。
3. **最後逐格驗證。** 開啟 [對應的 Jupyter Notebook](F5雙引擎與字幕開關_原始程式逐行講義.ipynb)，依相同段落編號對讀，再依序執行 10 個免 GPU 實驗。用兩個圖書館場景追蹤旁白、影片與字幕的輸出，並預測關閉字幕燒錄後還能在哪個檔案讀到台詞。F5 參數傳遞實驗使用測試替身，實際試聽需另外執行語音生成模型。

新版 Word 和 Notebook 請從上方連結分別下載。下方 ZIP 收錄原有技術簡報、逐頁講義與字幕工具。

## 教材下載

- [49 頁教學簡報（PPTX，含逐頁講者備註）](語音AI與多語字幕影片_技術教學簡報.pptx)
- [逐頁詳細講義（HTML，含簡報畫面與來源）](語音AI與多語字幕影片_逐頁教學講義.html)
- [完整教材包（ZIP）](語音AI與多語字幕影片_完整技術教材.zip)
- [開始使用與實作說明](開始使用與實作說明.txt)

HTML 請下載後用瀏覽器開啟，GitHub 檔案頁不會直接執行或呈現完整 HTML 網頁。內嵌圖片可離線閱讀，也可用瀏覽器列印成 PDF。

## 學習內容

語音合成技術演進、開源模型選型、多語翻譯、ASR 與字幕對齊、V1／V2 函式與資料流、影片時間軸、字幕軌與燒錄、部署與測試。

早期 V2 產生影片與獨立 SRT。新版 SubtitleToggle 在生成時決定是否把字幕燒入畫面，兩種設定都會輸出獨立的 `subtitles.srt`。若希望觀眾播放時能開關字幕，可用下方工具的 `soft` 指令，把 SRT 封裝成影片內的字幕軌。

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
