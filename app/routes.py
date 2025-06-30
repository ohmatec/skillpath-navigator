from flask import Blueprint, render_template, request, redirect, url_for, session
from app.services.skill_gap import analyze_skill_gap
import json
import os

main = Blueprint('main', __name__)

# หน้าแรก
@main.route('/')
def index():
    return render_template('index.html')

# หน้าแบบสอบถาม Skill Survey (GET + POST)
@main.route('/survey', methods=['GET', 'POST'])
def survey():
    # โหลดข้อมูลตำแหน่งและทักษะจากไฟล์ JSON
    json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'job_skills_mock.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        job_data = json.load(f)

    all_skills = sorted({ skill for job in job_data for skill in job['skills'] })

    if request.method == 'POST':
        selected = request.form.getlist('skills')
        session['user_skills'] = selected
        return redirect(url_for('main.result'))

    return render_template('form.html', skills=all_skills)

@main.route('/result')
def result():
    user_skills = session.get('user_skills', [])
    if not user_skills:
        return redirect(url_for('main.survey'))

    analysis = analyze_skill_gap(user_skills)
    return render_template('result.html', user_skills=user_skills, analysis=analysis)
