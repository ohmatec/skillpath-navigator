SkillPath Navigator

📌 Overview

SkillPath Navigator เป็น Web Application ที่ช่วยให้ผู้ใช้งานสามารถประเมินทักษะปัจจุบัน (user skills) เทียบกับความต้องการของตำแหน่งงานในตลาดเทคโนโลยีของไทย จากนั้นระบบจะวิเคราะห์ช่องว่างทักษะ (Skill Gap) และแนะนำเส้นทางการเรียนรู้ (Learning Path) เพื่อพร้อมเข้าสู่ตำแหน่งงานที่เหมาะสม

🎯 Key Features

Skill Survey: เก็บและประเมินทักษะที่ผู้ใช้มีผ่านแบบฟอร์ม

Skill Gap Analysis: เปรียบเทียบทักษะกับตำแหน่งงานจริง พร้อมคำนวณ % Match

Personalized Learning Path: แนะนำลิงก์แหล่งเรียนรู้ฟรีสำหรับทักษะที่ยังขาด

Dashboard Summary: สรุปตำแหน่งที่เหมาะสมที่สุด พร้อมรายละเอียดทักษะที่ควรเรียนเพิ่มเติม

🛠️ Tech Stack

Layer

Technology

Backend

Python 3.x, Flask

Frontend

HTML5, Tailwind CSS

Data & Logic

pandas, JSON files

Versioning

Git, GitHub

Deployment

Render (Free Tier)

🚀 Installation & Local Setup

Clone the repository

git clone https://github.com/<your-username>/skillpath-navigator.git
cd skillpath-navigator

Create and activate virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the application

python run.py

Access
เปิดเบราว์เซอร์ที่ http://127.0.0.1:5000/

🌐 Deployment (Free)

Create a GitHub repository และ Push โค้ดขึ้น GitHub

ลงทะเบียน บน Render.com ฟรี

Connect GitHub account และเลือก Repo skillpath-navigator

Configure Build & Start Commands:

Build Command: pip install -r requirements.txt

Start Command: python run.py

Deploy บน Render ฟรี (HTTPS พร้อม Domain ฟรีแบบ .onrender.com)

🎉 เมื่อ Deploy สำเร็จ แอปจะพร้อมใช้งานออนไลน์ทันที!

📄 Usage

เข้า /survey เพื่อเลือกทักษะ

ระบบจะนำไป /result วิเคราะห์ตำแหน่งงานและ Gap

เข้า /dashboard เพื่อดูสรุปและแผนการเรียนรู้

🤝 Contributing

Fork repository และสร้าง branch ใหม่ เช่น feature/your-feature

ทำงานและ Commit แบบมีความหมาย (e.g. feat: add X)

Pull Request พร้อมคำอธิบายชัดเจน

📜 License

MIT License © 2025 Your Name
