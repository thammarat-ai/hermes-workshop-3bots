#!/usr/bin/env python3
"""สร้างไฟล์ PDF ตัวอย่างให้นิสิตลองสรุปในขั้น พี่ติว (study-coach)"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# พยายามลงทะเบียนฟอนต์ไทย (ถ้ามีในระบบ) ถ้าไม่มีจะใช้ฟอนต์ default
THAI_FONT = None
for cand in [
    "C:/Windows/Fonts/LeelawUI.ttf",
    "C:/Windows/Fonts/Tahoma.ttf",
]:
    try:
        pdfmetrics.registerFont(TTFont("thai", cand))
        THAI_FONT = "thai"
        break
    except Exception:
        continue

styles = getSampleStyleSheet()
title_style = ParagraphStyle("title", parent=styles["Title"], fontName=THAI_FONT or "Helvetica",
                             fontSize=22, textColor=colors.HexColor("#1f3a5f"), spaceAfter=12)
h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName=THAI_FONT or "Helvetica",
                    fontSize=14, textColor=colors.HexColor("#2a5d8f"), spaceBefore=10, spaceAfter=6)
body = ParagraphStyle("body", parent=styles["BodyText"], fontName=THAI_FONT or "Helvetica",
                      fontSize=11, leading=16)

doc = SimpleDocTemplate("sample_lecture.pdf", pagesize=A4,
                        leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
E = []

E.append(Paragraph("บทที่ 4: ระบบแนะนำสินค้า (Recommendation System)", title_style))
E.append(Paragraph("วิชา Data Science สำหรับธุรกิจ — เอกสารประกอบการบรรยาย", body))
E.append(Spacer(1, 0.3*cm))

E.append(Paragraph("1. แนวคิดพื้นฐาน", h2))
E.append(Paragraph(
    "ระบบแนะนำสินค้า (Recommendation System) คือโมเดลที่ช่วยทำนายว่าผู้ใช้คนใดน่าจะสนใจสินค้าใด "
    "โดยวิเคราะห์จากพฤติกรรมในอดีต เช่น การคลิก การซื้อ หรือการให้คะแนน "
    "ระบบนี้ถูกใช้อย่างแพร่หลายในแพลตฟอร์มสตรีมมิง อีคอมเมิร์ซ และโซเชียลมีเดีย", body))

E.append(Paragraph("2. วิธีหลัก 3 ประเภท", h2))
E.append(Paragraph(
    "2.1 Collaborative Filtering ทำงานโดยดูพฤติกรรมผู้ใช้หลายคนที่มีรสนิยมคล้ายกัน "
    "แล้วแนะนำสินค้าที่ผู้ใช้กลุ่มนั้นชอบให้กัน", body))
E.append(Paragraph(
    "2.2 Content-Based Filtering ดูคุณลักษณะของสินค้าเอง เช่น หมวดหมู่ ราคา แท็ก "
    "แล้วแนะนำสินค้าที่คล้ายกับที่ผู้ใช้นั้นเคยสนใจ", body))
E.append(Paragraph(
    "2.3 Hybrid ผสมทั้งสองวิธีเพื่อลดจุดอ่อน เช่น ปัญหา cold-start (สินค้าใหม่ไม่มีข้อมูล)", body))

E.append(Paragraph("3. ตัวอย่างในโลกจริง", h2))
data = [
    ["แพลตฟอร์ม", "วิธีที่ใช้", "ผลลัพธ์"],
    ["Netflix", "Collaborative + Hybrid", "รายได้เพิ่มจากการดูต่อเนื่อง"],
    ["Shopee", "Content-Based + Hybrid", "เพิ่มอัตราการคลิกสินค้าแนะนำ"],
    ["Spotify", "Collaborative (Discover Weekly)", "ผู้ใช้ฟังเพลงใหม่มากขึ้น"],
]
t = Table(data, colWidths=[4*cm, 6*cm, 6*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2a5d8f")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,-1), THAI_FONT or "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#eef3f8")]),
]))
E.append(t)
E.append(Spacer(1, 0.3*cm))

E.append(Paragraph("4. ข้อจำกัดที่ควรระวัง", h2))
E.append(Paragraph(
    "ระบบแนะนำอาจเกิดอคติ (bias) ได้ เช่น แนะนำแต่สินค้าขายดีอยู่แล้ว "
    "ทำให้สินค้าใหม่หรือกลุ่มน้อยไม่มีโอกาสแสดงผล นอกจากนี้ยังมีประเด็นความเป็นส่วนตัว "
    "หากจัดเก็บพฤติกรรมผู้ใช้โดยไม่เปิดเผย", body))

E.append(Paragraph("5. งานที่ให้ทำ (Assignment)", h2))
E.append(Paragraph(
    "1) อธิบายความต่างระหว่าง Collaborative และ Content-Based อย่างละ 2 ประโยค<br/>"
    "2) ยกตัวอย่างแพลตฟอร์มที่นักศึกษาใช้ประจำ แล้วระบุว่าน่าจะใช้ระบบแนะนำแบบใด<br/>"
    "3) เสนอวิธีลดอคติในระบบแนะนำสินค้า 1 วิธี<br/>"
    "ส่งภายในวันศุกร์นี้ 23.59 น. ทางระบบ LMS", body))

doc.build(E)
print("สร้างไฟล์: sample_lecture.pdf")
