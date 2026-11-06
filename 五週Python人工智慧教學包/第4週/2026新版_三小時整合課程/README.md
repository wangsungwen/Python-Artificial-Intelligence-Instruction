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




## 已發布 Office 成品（2026-11-06）

已將以下**真正的 Office 檔案**直接提交到 GitHub `main`，無須先執行產生器：

- [第四週_教師手冊.docx](第四週_教師手冊.docx)：Word 教師手冊；課程概念、六單元教師示範、實作與驗收、逐行程式說明。
- [第四週_文字可編輯簡報.pptx](第四週_文字可編輯簡報.pptx)：24 頁 16:9 校園學術雜誌風格版，文字及色塊為原生 PowerPoint 物件。
- [第四週_語音AI與多語字幕影片_完整實作.ipynb](第四週_語音AI與多語字幕影片_完整實作.ipynb)：Python/Colab 實作。

**版本註記：**本次 GitHub 發布的 Word／PPTX 是依第四週課綱重新生成並直接寫入倉庫的 Office 版本，不保證與對話中先前提供的本機設計檔逐位元相同。

`build_week4_documents.py` 仍保留為可重複產生文件的教學程式；執行產生器可能覆蓋這次上傳的成品，操作前請先備份。
