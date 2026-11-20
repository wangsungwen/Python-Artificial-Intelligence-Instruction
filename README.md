## 第四週 F5-TTS 真實生成同步教材（2026-11-09）

已新增 [第四週 F5-TTS 真實語音、字幕與影片合成](五週Python人工智慧教學包/第4週/F5TTS_真實語音_2026新版/)，包含 **12 個 Colab 實作單元（IPYNB）**、**逐行程式教學 Word**、**24 頁可編輯 PPTX** 與 **三份同步教材 ZIP**。教學版採 F5TTS 官方 Python API 實際生成 WAV，再產生 SRT、PNG、MP4；需 Colab T4 GPU 及 FFmpeg。**程式尚未在 Colab GPU 完成端到端執行驗證**，字幕為人工編寫、按場景對齊，並非自動翻譯。

# 五週 Python 人工智慧教學包

每週 180 分鐘，含 10 分鐘休息。前三週練習 Python 語法，第 4 週用場景資料製作字幕，第 5 週用影像資料訓練分類器。

## 開始使用

初次使用 Notebook，可先跟著[Python 與 Notebook 入門](00_Python%E8%88%87Notebook%E5%85%A5%E9%96%80.ipynb)練習執行儲存格。上課時從下表開啟當週簡報，再點「在 Colab 開啟」動手操作。需要離線教材時，可[下載五週完整教材 ZIP](https://github.com/wangsungwen/Python-Artificial-Intelligence-Instruction/archive/refs/heads/main.zip)。

## 每週教材

| 週次與主題 | 課堂實作 | 簡報 | 筆記本 |
| --- | --- | --- | --- |
| 第 1 週｜Python 入門與資料型別 | 用變數保存資料，觀察型別如何影響運算結果。 | [教學簡報](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC1%E9%80%B1/%E7%AC%AC%E4%B8%80%E9%80%B1%E8%AC%9B%E7%BE%A9PPTX.pptx) | [開啟筆記本](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC1%E9%80%B1/%E7%AC%AC%E4%B8%80%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC1%E9%80%B1/%E7%AC%AC%E4%B8%80%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94.ipynb) |
| 第 2 週｜輸入、輸出與條件判斷 | 用 `input()` 讀取資料、轉換型別，再用條件式決定輸出。 | [教學簡報](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC2%E9%80%B1/%E7%AC%AC%E4%BA%8C%E9%80%B1%E8%AC%9B%E7%BE%A9PPTX.pptx) | [開啟筆記本](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC2%E9%80%B1/%E7%AC%AC%E4%BA%8C%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC2%E9%80%B1/%E7%AC%AC%E4%BA%8C%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94.ipynb) |
| 第 3 週｜迴圈、串列與函式 | 把重複操作寫成迴圈，以串列整理資料，封裝成可重用的函式。 | [教學簡報](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC3%E9%80%B1/%E7%AC%AC%E4%B8%89%E9%80%B1%E8%AC%9B%E7%BE%A9PPTX.pptx) | [開啟筆記本](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC3%E9%80%B1/%E7%AC%AC%E4%B8%89%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94%28new%29.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC3%E9%80%B1/%E7%AC%AC%E4%B8%89%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94%28new%29.ipynb) |
| 第 4 週｜語音 AI 與多語字幕影片 | 把三個場景整理成多語台詞、字幕時間軸與檢查報告。 | [教學簡報](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC4%E9%80%B1/2026%E6%96%B0%E7%89%88_%E4%B8%89%E5%B0%8F%E6%99%82%E6%95%B4%E5%90%88%E8%AA%B2%E7%A8%8B/%E7%AC%AC%E5%9B%9B%E9%80%B1_%E6%96%87%E5%AD%97%E5%8F%AF%E7%B7%A8%E8%BC%AF%E7%B0%A1%E5%A0%B1.pptx) | [開啟筆記本](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC4%E9%80%B1/2026%E6%96%B0%E7%89%88_%E4%B8%89%E5%B0%8F%E6%99%82%E6%95%B4%E5%90%88%E8%AA%B2%E7%A8%8B/%E7%AC%AC%E5%9B%9B%E9%80%B1_%E8%AA%9E%E9%9F%B3AI%E8%88%87%E5%A4%9A%E8%AA%9E%E5%AD%97%E5%B9%95%E5%BD%B1%E7%89%87_%E5%AE%8C%E6%95%B4%E5%AF%A6%E4%BD%9C.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC4%E9%80%B1/2026%E6%96%B0%E7%89%88_%E4%B8%89%E5%B0%8F%E6%99%82%E6%95%B4%E5%90%88%E8%AA%B2%E7%A8%8B/%E7%AC%AC%E5%9B%9B%E9%80%B1_%E8%AA%9E%E9%9F%B3AI%E8%88%87%E5%A4%9A%E8%AA%9E%E5%AD%97%E5%B9%95%E5%BD%B1%E7%89%87_%E5%AE%8C%E6%95%B4%E5%AF%A6%E4%BD%9C.ipynb) |
| 第 5 週｜AI 分類與成果發表 | 用影像的 RGB 平均值訓練最近中心分類器，以保留測試集檢查結果。 | [教學簡報](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC5%E9%80%B1/W05_%E6%95%99%E5%AD%B8%E7%B0%A1%E5%A0%B1.pptx) | [開啟筆記本](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC5%E9%80%B1/W05_%E5%AD%B8%E5%93%A1%E5%AF%A6%E4%BD%9C.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC5%E9%80%B1/W05_%E5%AD%B8%E5%93%A1%E5%AF%A6%E4%BD%9C.ipynb) |

## 補充教材｜YOLO 車牌辨識

**公開模型推論版**：[在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E8%A3%9C%E5%85%85%E6%95%99%E6%9D%90/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98_Python%E8%AA%9E%E6%B3%95%E4%BA%92%E5%8B%95%E5%BC%8F%E9%80%90%E5%8D%80%E5%A1%8A%E5%AF%A6%E4%BD%9C.ipynb) · [下載 Word 手冊](%E8%A3%9C%E5%85%85%E6%95%99%E6%9D%90/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98_Python%E8%AA%9E%E6%B3%95%E4%BA%92%E5%8B%95%E5%BC%8F%E5%B0%88%E6%A1%88%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A.docx?raw=true)。首次連網下載 YOLOv8 車牌權重與 EasyOCR，執行第 0 單元；準備自有標註資料後可選擇訓練 YOLO11。新版已通過語法檢查，尚未在 Colab 驗證端到端推論。

**原免權重教學版**

以 13 個單元練習 Python 語法與雙階段辨識。課堂預設是免 GPU、免模型權重的合成示範，可驗收圖片標註與影片逐幀輸出；真實辨識需另備可信任的車牌與字元模型權重。

- [Colab 筆記本](%E8%A3%9C%E5%85%85%E6%95%99%E6%9D%90/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98_Python%E9%80%90%E5%8D%80%E5%A1%8A%E5%AF%A6%E4%BD%9C_%E8%AA%B2%E5%A0%82%E4%BF%AE%E6%AD%A3%E7%89%88.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E8%A3%9C%E5%85%85%E6%95%99%E6%9D%90/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98_Python%E9%80%90%E5%8D%80%E5%A1%8A%E5%AF%A6%E4%BD%9C_%E8%AA%B2%E5%A0%82%E4%BF%AE%E6%AD%A3%E7%89%88.ipynb)
- [下載 Word 教學手冊](%E8%A3%9C%E5%85%85%E6%95%99%E6%9D%90/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98/YOLO%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98_Python%E8%AA%9E%E6%B3%95%E4%BA%92%E5%8B%95%E5%BC%8F%E5%B0%88%E6%A1%88%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A_v2.docx?raw=true)

免權重的 28 個程式格已在本機 CPU 順序執行。尚未用真實模型權重或在 Colab 上實測。

## 各週操作與延伸練習

1. **第 1 週**使用預設的 `INTERACTIVE=False` 可依序執行示範。要逐題輸入自己的資料，將設定改為 `True` 並重新執行設定格。
2. **第 2 週**預設開啟互動輸入，請逐格操作。遇到字串加整數等錯誤示範，先讀例外訊息，再手動執行下一格。
3. **第 3 週**逐格輸入資料並觀察迴圈終止條件。第 2、3 週直接呼叫 `input()` 的儲存格都需要手動輸入。完成函式單元後，可用[前三週綜合練習（10 題）](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC3%E9%80%B1/%E7%AC%AC%E4%B8%80%E8%87%B3%E4%B8%89%E9%80%B1_%E8%AA%B2%E5%BE%8C%E7%B7%B4%E7%BF%92%E9%A1%8C%E7%9B%AE%E5%96%AE_%E5%85%B1%E5%8D%81%E9%A1%8C.ipynb)自我檢核。
4. **第 4 週**先依[三小時課程導讀](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC4%E9%80%B1/2026%E6%96%B0%E7%89%88_%E4%B8%89%E5%B0%8F%E6%99%82%E6%95%B4%E5%90%88%E8%AA%B2%E7%A8%8B/README.md)在 CPU 上產生 JSON 與 SRT，再循[技術教材導讀](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC4%E9%80%B1/%E8%AA%9E%E9%9F%B3AI%E8%88%87%E5%A4%9A%E8%AA%9E%E5%AD%97%E5%B9%95%E5%BD%B1%E7%89%87_%E6%8A%80%E8%A1%93%E6%95%99%E6%9D%90/README.md)閱讀 F5 語音合成與字幕開關的原始碼。[Word 逐行講義](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC4%E9%80%B1/%E8%AA%9E%E9%9F%B3AI%E8%88%87%E5%A4%9A%E8%AA%9E%E5%AD%97%E5%B9%95%E5%BD%B1%E7%89%87_%E6%8A%80%E8%A1%93%E6%95%99%E6%9D%90/F5%E9%9B%99%E5%BC%95%E6%93%8E%E8%88%87%E5%AD%97%E5%B9%95%E9%96%8B%E9%97%9C_%E5%8E%9F%E5%A7%8B%E7%A8%8B%E5%BC%8F%E9%80%90%E8%A1%8C%E8%AC%9B%E7%BE%A9.docx)可搭配[10 個免 GPU 實驗](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC4%E9%80%B1/%E8%AA%9E%E9%9F%B3AI%E8%88%87%E5%A4%9A%E8%AA%9E%E5%AD%97%E5%B9%95%E5%BD%B1%E7%89%87_%E6%8A%80%E8%A1%93%E6%95%99%E6%9D%90/F5%E9%9B%99%E5%BC%95%E6%93%8E%E8%88%87%E5%AD%97%E5%B9%95%E9%96%8B%E9%97%9C_%E5%8E%9F%E5%A7%8B%E7%A8%8B%E5%BC%8F%E9%80%90%E8%A1%8C%E8%AC%9B%E7%BE%A9.ipynb)使用。實際生成模型旁白另需準備模型權重及對應執行環境。
5. **第 5 週**先在學員筆記本比較預測類別與正確標籤，記錄一次判對或判錯的原因，再對照[講師解答](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC5%E9%80%B1/W05_%E8%AC%9B%E5%B8%AB%E8%A7%A3%E7%AD%94.ipynb)。授課者可搭配[逐字講稿](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC5%E9%80%B1/W05_%E8%AC%9B%E5%B8%AB%E9%80%90%E5%AD%97%E8%AC%9B%E7%A8%BF.docx)帶領成果發表。

## 在自己的電腦執行

下載並解壓縮教材，在含有 [requirements.txt](%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/requirements.txt) 的資料夾開啟終端機，執行下列指令安裝課程套件，再以 Jupyter 開啟當週筆記本。Windows 教室也可使用[一鍵安裝工具](Windows_Python%E6%95%99%E5%AE%A4%E4%B8%80%E9%8D%B5%E5%AE%89%E8%A3%9D.zip)。

```sh
python -m pip install -r requirements.txt
```
