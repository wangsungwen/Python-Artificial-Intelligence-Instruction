# 五週 Python 人工智慧教學包

供課程學員下載的五週 Python 人工智慧教材。每週 180 分鐘，含 10 分鐘休息。

## 下載教材

**[點此一次下載全部教材（ZIP）](https://github.com/wangsungwen/Python-Artificial-Intelligence-Instruction/archive/refs/heads/main.zip)**

下載後先解壓縮，再進入「五週Python人工智慧教學包」資料夾。也可以使用本頁上方的 **Code → Download ZIP**。

## 開始使用

1. 先閱讀 `00_課程總覽與授課指南.docx` 及 `README_先讀我.txt`。
2. 第 1～3 週開啟對應資料夾中的 `第一週_Colab完整教學與習題解答.ipynb`、`第二週_Colab完整教學與習題解答.ipynb` 或 `第三週_Colab完整教學與習題解答.ipynb`；第 4、5 週使用原有學員實作與講師解答筆記本。
3. 使用支援 Jupyter Notebook 的環境開啟 `.ipynb`。若在自己的電腦執行，請先在教材資料夾中安裝套件：

   ```sh
   python -m pip install -r requirements.txt
   ```

## 教材目錄

| 週次 | 教材資料夾 |
| --- | --- |
| 第 1 週 | [開啟教材](五週Python人工智慧教學包/第1週/) |
| 第 2 週 | [開啟教材](五週Python人工智慧教學包/第2週/) |
| 第 3 週 | [開啟教材](五週Python人工智慧教學包/第3週/) |
| 第 4 週 | [開啟教材](五週Python人工智慧教學包/第4週/) |
| 第 5 週 | [開啟教材](五週Python人工智慧教學包/第5週/) |

第 1～3 週各提供一份新版講義 PPTX 與一份整合圖片、文字、可執行範例、練習區及解答的 Colab 筆記本。第 4、5 週保留教學簡報、學員實作、講師逐字講稿及講師解答。學員建議先完成練習，再參考解答。

課程總覽 DOCX 與第 1、3 週既有逐字講稿保留供歷史參考，其課程內容及檔名可能與新版第 1～3 週不同；前三週請以新版 PPTX 與 Colab 筆記本為準。

核心實作資料由程式產生，不需要攝影機、帳號、API 金鑰或模型下載。第 5 週色彩分類器為教材概念的簡化新增實作，非教材原有深度學習模型。

## 第一至三週新版 Colab 教材

| 週次 | 講義 | Colab 筆記本 | 內容 |
| --- | --- | --- | --- |
| 第 1 週 | [下載 PPTX](五週Python人工智慧教學包/第1週/第一週講義PPTX.pptx) | [下載筆記本](五週Python人工智慧教學包/第1週/第一週_Colab完整教學與習題解答.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC1%E9%80%B1/%E7%AC%AC%E4%B8%80%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94.ipynb) | 131 頁講義、3 組原題解答與 4 組補充練習 |
| 第 2 週 | [下載 PPTX](五週Python人工智慧教學包/第2週/第二週講義PPTX.pptx) | [下載筆記本](五週Python人工智慧教學包/第2週/第二週_Colab完整教學與習題解答.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC2%E9%80%B1/%E7%AC%AC%E4%BA%8C%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94.ipynb) | 117 頁講義、7 題解答 |
| 第 3 週 | [下載 PPTX](五週Python人工智慧教學包/第3週/第三週講義PPTX.pptx) | [下載筆記本](五週Python人工智慧教學包/第3週/第三週_Colab完整教學與習題解答.ipynb) · [在 Colab 開啟](https://colab.research.google.com/github/wangsungwen/Python-Artificial-Intelligence-Instruction/blob/main/%E4%BA%94%E9%80%B1Python%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%95%99%E5%AD%B8%E5%8C%85/%E7%AC%AC3%E9%80%B1/%E7%AC%AC%E4%B8%89%E9%80%B1_Colab%E5%AE%8C%E6%95%B4%E6%95%99%E5%AD%B8%E8%88%87%E7%BF%92%E9%A1%8C%E8%A7%A3%E7%AD%94.ipynb) | 150 頁講義、13 題解答 |

筆記本已內嵌圖片並保留執行輸出，不需另傳 PPTX；使用 Python 3.10 以上的一般 CPU 執行階段即可。第 1 週預設 `INTERACTIVE=False` 可全部執行；改為 `True` 並重跑設定格，可逐題自行輸入。第 1 週已在 Python 3.12 的乾淨核心執行驗證。

第 2 週已替換為使用者提供的更新版，原樣保留程式及輸出，已檢查筆記本格式，未重新執行全本。新版新增直接呼叫 `input()` 的儲存格，不受 `INTERACTIVE` 開關控制，請逐格操作並依提示輸入；`score + 10`（字串加整數）及 `int("3.14")` 等錯誤示範會產生例外，全部執行到此會中斷，閱讀後可手動執行下一格。

第 3 週已替換為使用者提供的更新版，原樣保留程式及輸出，已檢查筆記本格式，未重新執行全本。新版預設 `INTERACTIVE=True`，請逐格操作並依提示輸入。設為 `False` 並重跑設定格，只會切換使用 `make_input()` 的範例；直接呼叫 `input()` 的儲存格仍會等待輸入。

第一週主題為 Python 入門、開發環境、程式邏輯、變數與資料型別；第二週主題為輸出、輸入、運算式與選擇敘述；第三週為迴圈、串列與函式。舊版第一、三週分離式學員／講師筆記本，以及第二週世界時鐘、計算機已由新版取代，舊檔可從 Git 歷史查閱。

上方「全部教材 ZIP」與 **Code → Download ZIP** 都依 `main` 分支即時產生，包含本次新版檔案。`Windows_Python教室一鍵安裝.zip` 是安裝工具，不是教材壓縮包。

## 舊版章後習題與詳解補充教材

以下為 2026-10-18 舊版更新紀錄，第 1～3 週已改採上方新版，不再適用以下舊版題數。當時每週學員版與講師版筆記本末段均加入對應的原書習題與詳解，共108題。原有課堂內容保留，補充題供課後複習；進階題標示「延伸練習」。

| 週次 | 對應章節 | 題數 |
| --- | --- | ---: |
| 第1週 | 第1–3章：Python起步、變數與運算 | 20 |
| 第2週 | 第4–5章：條件與迴圈 | 16 |
| 第3週 | 第6–9章：函數、容器、檔案與模組 | 32 |
| 第4週 | 第10章：OpenCV與NumPy | 8 |
| 第5週 | 第11–16章：AI概念與應用延伸 | 32 |

學員版可展開各題的「參考詳解」，講師版直接顯示解答。題目出自「中文習題WORD檔(全).doc」，原解出自「章後習題詳解(全).doc」，並保留原章題號、附圖與課本章節指引。21項「教學補充與勘誤」與原解分開呈現，包含複利利率、繩長邊界、非零乘積及分段計費等修正。

第1至9章各附一組提供的 Copilot 輔助學習提示詞；第4、5週另附配合影像與AI主題新增的提示詞。原詳解中需要圖片、影片、攝影機、Office或模型的範例列為閱讀參考，執行前須另備相符環境；這些範例以 Markdown 呈現，不影響原課堂程式的「全部執行」。
