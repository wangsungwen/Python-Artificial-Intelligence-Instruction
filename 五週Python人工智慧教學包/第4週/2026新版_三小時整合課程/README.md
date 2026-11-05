# 第四週新版：三小時 Python × 語音 AI × 多語字幕影片

本資料夾與原有「語音AI與多語字幕影片_技術教材」並存，不覆蓋原先 49 頁技術簡報與字幕工具。

## 180 分鐘課堂節奏

| 時段 | 學習內容 | 主要輸出 |
|---|---|---|
| 0–30 | import、變數、Path | 執行環境 |
| 30–60 | list、dict、for | 三場景 |
| 60–90 | def、if、raise、except | 資料防呆 |
| 90–120 | f-string、divmod、SRT | 字幕與 JSON |
| 120–150 | Colab 與既有 V2 輸出對照 | 檔案檢查 |
| 150–180 | Hugging Face Spaces 展示與驗收 | run_report.json |

Notebook 可在一般 Python 3／Colab CPU 下執行。英文範例旁白是手寫內容，不代表模型翻譯。SRT 是「場景預定時間軸」，不是 ASR forced alignment。語音克隆、翻譯與影片生成須另行測試依賴與授權。

## 檔案說明
- `第四週_語音AI與多語字幕影片_完整實作.ipynb`：學生可逐格執行版本
- `build_week4_documents.py`：從上方課程架構建立可編輯 Word 和 PPTX
- `第四週_教師手冊.docx`：三小時教學稿（由 generator 產生）
- `第四週_文字可編輯簡報.pptx`：PowerPoint 原生文字與圖形（由 generator 產生）

線上原專案：https://github.com/wangsungwen/Python-Artificial-Intelligence-Instruction
Hugging Face V2：https://huggingface.co/spaces/wangsongwen/Multilingual-Video-Studio-V2
