# -*- coding: utf-8 -*-
"""從第四週課程綱要產生可編輯 Word/PPTX。需 python-docx、python-pptx。"""
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor
from pptx import Presentation
from pptx.util import Inches, Pt as PPTPt
from pptx.dml.color import RGBColor as C
from pptx.enum.shapes import MSO_SHAPE
OUT=Path(__file__).parent
TOPICS=[
("00–30","專案架構與環境","import、變數、Path","輸出目錄"),
("30–60","場景與多語資料","list、dict、for","scene_plan.json"),
("60–90","函式化與例外處理","def、if、raise、except","防呆測試"),
("90–120","時間軸與 SRT","divmod、f-string、write_text","subtitles.srt"),
("120–150","Colab 與 V2 系統銜接","Notebook、檔案","輸出檢查"),
("150–180","Hugging Face 展示與驗收","UI、Callback、assert","run_report.json")]
d=Document(); d.add_heading("第四週｜Python × 語音 AI × 多語字幕影片",0)
d.add_paragraph("180 分鐘教師手冊｜前三週 Python 語法整合｜Colab CPU 可實作｜Hugging Face 延伸展示")
d.add_heading("學習定位",1)
d.add_paragraph("以場景資料、Python 函式、SRT 字幕與 JSON 成果練習為主；不宣稱完成 TTS、ASR 或翻譯。")
for t,name,syntax,output in TOPICS:
 d.add_heading(t+" 分鐘｜"+name,1)
 d.add_paragraph("語法： "+syntax)
 d.add_paragraph("10 分鐘：教師示範程式碼、輸入與輸出。")
 d.add_paragraph("15 分鐘：學員執行對應 Notebook，修改一個欄位並觀察結果。")
 d.add_paragraph("5 分鐘：驗收 "+output+"；未完成者保存目前進度，下一段從範例輸出接續。")
 d.add_paragraph("教師提問：這一段的輸入是什麼？使用何種資料結構？程式在哪裡驗證錯誤？")
d.add_heading("成果評分",1)
d.add_paragraph("Python 語法 30；場景資料與驗證 25；SRT 時間與檔案 25；紀錄與限制說明 20。")
d.add_heading("技術範圍",1)
d.add_paragraph("原有 GitHub 工具 subtitle_tools.py 可產生 SRT、soft／burn 影片字幕，soft／burn 需要 FFmpeg。學員先完成本教材純 Python JSON/SRT，再研究既有工具不同的 cues schema。")
d.save(OUT/"第四週_教師手冊.docx")
p=Presentation();p.slide_width=Inches(13.333);p.slide_height=Inches(7.5)
navy=C(22,43,70); teal=C(25,132,146);orange=C(223,137,83);paper=C(247,247,243)
def tb(sl,s,x,y,w,h,sz,color,b=False):
 box=sl.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
 tf=box.text_frame;tf.word_wrap=True;tf.text=s
 for para in tf.paragraphs:
  para.font.name="Microsoft JhengHei";para.font.size=PPTPt(sz);para.font.bold=b;para.font.color.rgb=color
def slide(title,subtitle,left,right,index):
 sl=p.slides.add_slide(p.slide_layouts[6]);sh=sl.shapes.add_shape(MSO_SHAPE.RECTANGLE,0,0,p.slide_width,p.slide_height)
 sh.fill.solid();sh.fill.fore_color.rgb=paper;sh.line.fill.background()
 bar=sl.shapes.add_shape(MSO_SHAPE.RECTANGLE,0,0,p.slide_width,Inches(.14))
 bar.fill.solid();bar.fill.fore_color.rgb=teal;bar.line.fill.background()
 tb(sl,"WEEK 04  /  CAMPUS AI LAB",.6,.37,11,.35,13,teal,True)
 tb(sl,title,.6,.9,12,1,32,navy,True);tb(sl,subtitle,.6,1.94,12,.55,16,teal)
 for x,txt,color in [(.62,left,navy),(6.82,right,teal)]:
  sh=sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(2.75),Inches(5.76),Inches(3.5))
  sh.fill.solid();sh.fill.fore_color.rgb=color;sh.line.fill.background()
  tb(sl,txt,x+.28,3.04,5.15,2.9,19,C(255,255,255))
 tb(sl,f"{index:02}  •  三小時邊教邊做",.7,6.9,11,.35,13,navy)
slide("第四週｜Python × 語音 AI","180 分鐘｜三週語法延伸","場景資料 → 防呆函式 → 字幕 → JSON","Colab 核心操作\nHugging Face V2 延伸展示",1)
slide("六單元 × 30 分","每段：講 10 分／做 15 分／驗 5 分","\n".join(t+"  "+name for t,name,_,_ in TOPICS[:3]),"\n".join(t+"  "+name for t,name,_,_ in TOPICS[3:]),2)
for i,(t,name,syntax,output) in enumerate(TOPICS,3):
 slide(name,t+" 分鐘｜"+syntax,"概念與語法\n\n"+syntax+"\n\n用前三週基礎理解本單元。","操作與驗收\n\n打開同名 Notebook 章節。\n修改一行 → 執行 → 存檔\n成果："+output,i)
 slide(name+"｜實作",t+" 分鐘｜TASK · CHECK","TASK\n\n先預測程式的輸出，再執行與修改輸入。","CHECK\n\n交付 "+output+"\n\n說明資料如何經過 Python 處理。",i+6)
for i,(t,name,syntax,output) in enumerate(TOPICS,17):
 slide(name+"｜程式語法解析",t+" 分鐘｜逐行理解","關鍵字與資料型別\\n\\n"+syntax+"\\n\\n從輸入、運算、輸出逐行閱讀。","實作挑戰\\n\\n修改參數並重新執行。\\n\\n驗收結果："+output,i)
slide("系統邊界與持續學習","安全、授權、驗證不可省略","本週：JSON、SRT、時間軸\nCPU 逐格練習通過","延伸：TTS／ASR／翻譯／MP4\n需另外測試模型和授權",15)
slide("成果評分與下一週延伸","語法 30｜資料 25｜字幕 25｜紀錄 20","交付三個檔案：\nscene_plan.json\nsubtitles.srt\nrun_report.json","下週持續：\nCSV 批次輸入\nGradio／FFmpeg／部署",16)
p.save(OUT/"第四週_文字可編輯簡報.pptx")
slide("實作成果展示｜JSON 與 SRT","課堂作品的最小交付標準","場景 ID、語言欄位、旁白與 duration","檔案：scene_plan.json\\nsubtitles.srt\\nrun_report.json",23)
slide("結語｜從 Python 到多語影片","下一週延伸與可持續學習","Python 入門 → 資料驗證 → 多語字幕","模型 TTS/ASR/翻譯與 MP4 另行驗證",24)
assert len(p.slides)==24\nprint("完成",len(p.slides),"頁")
