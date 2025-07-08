# 🚀 SkillPath Navigator  
> ระบบวิเคราะห์ตำแหน่งงานที่เหมาะสมตามทักษะ พร้อมแนะนำเส้นทางการเรียนรู้เฉพาะบุคคล

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![Tailwind](https://img.shields.io/badge/UI-TailwindCSS-blueviolet)
![Status](https://img.shields.io/badge/Status-MVP--Completed-brightgreen)

---

## 🎯 แนวคิดหลัก

**SkillPath Navigator** คือ Web Application สำหรับช่วยวิเคราะห์ว่า  
> ✨ “จากทักษะที่คุณมีตอนนี้ – งานไหนเหมาะที่สุด?”  
> และ ✨ “ควรเรียนรู้อะไรต่อไป เพื่อให้พร้อมสมัครงานจริง?”

ออกแบบโดยเน้น:  
- ✍️ ฝึกฝนกระบวนการพัฒนา Software Engineering แบบมีโครงสร้าง  
- 📈 เชื่อมโยงความต้องการในตลาดงานสายเทคโนโลยีไทย  
- 💼 เหมาะสำหรับใช้เป็น **Portfolio สำหรับสมัครงานในตำแหน่ง Junior Developer / Web Developer**

---

## 🛠️ เทคโนโลยีที่ใช้

| ด้าน        | เทคโนโลยี             | เหตุผลที่เลือก                                       |
|-------------|------------------------|-------------------------------------------------------|
| Backend     | Python + Flask         | Framework เบาแต่ยืดหยุ่น เหมาะกับ MVP               |
| Frontend    | HTML + TailwindCSS     | สร้าง UI เรียบหรูแบบมืออาชีพ                        |
| Logic Layer | Custom Skill Analyzer  | วิเคราะห์ Skill Gap ได้แม่นยำ เข้าใจง่าย           |
| Hosting     | Render (หรือ Railway)  | ฟรี 100% เหมาะกับผู้เริ่มต้น                        |

---

## 📦 คุณสมบัติหลัก (MVP)

- ✅ ฟอร์มเลือกทักษะที่ผู้ใช้มี
- ✅ วิเคราะห์ตำแหน่งงานที่เหมาะจากฐานข้อมูล
- ✅ แสดงทักษะที่ตรง / ควรพัฒนา
- ✅ แนะนำเส้นทางการเรียนรู้แบบลิงก์
- ✅ Dashboard สรุปภาพรวมดูดี (สไตล์ Apple)

---

## 📈 โครงสร้างโปรเจกต์

```bash
skillpath-navigator/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html          # หน้าแรก
│   │   ├── form.html           # แบบฟอร์มเลือกทักษะ
│   │   ├── result.html         # รายงานหลายตำแหน่ง
│   │   ├── dashboard.html      # หน้าสรุปแบบหรู
│   ├── services/
│   │   ├── analyzer.py
│   │   ├── skill_gap.py
│   │   ├── learning_path.py
├── run.py
├── requirements.txt
├── .gitignore
├── README.md


🧪 วิธีติดตั้งและใช้งาน (Local)
# Clone โครงการ
git clone https://github.com/your-username/skillpath-navigator.git
cd skillpath-navigator

# สร้าง virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# ติดตั้ง dependencies
pip install -r requirements.txt

# รันแอป
python run.py

เปิดเบราว์เซอร์ที่: http://127.0.0.1:5000


💡 จุดเด่นทางวิศวกรรม
    ✅ Code แยกส่วน (Modular) → พร้อมต่อยอด

    ✅ ใช้ Git อย่างเป็นระบบ: Branch, Commit message ดี

    ✅ หน้า UI ใช้ Tailwind แบบดูน่าเชื่อถือ

    ✅ เข้าใจ Skill Gap และแนะนำ Learning Path อย่างชัดเจน

🔧 ส่วนต่อยอด (Stretch Goals)
    🔐 เพิ่มระบบ Login/Profile

    📄 Export Dashboard เป็น PDF/Text

    🧠 เชื่อมต่อ AI API วิเคราะห์ Resume จริง

    🔎 ดึง Job จาก API จริง (JobsDB, RapidAPI)

🙋‍♂️ ผู้พัฒนา
    โอม วัฒนวิกย์กรรม

    พัฒนาเพื่อฝึกฝนกระบวนการ Software Engineering และสร้างผลงานที่พร้อมใช้งานจริงในสายงาน IT

📫 ติดต่อ / เชื่อมต่อ
    GitHub: github.com/ohmatec

    Email: Ohmatec10@gmail.com

