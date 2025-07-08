import json
import os
from app.services.learning_path import get_learning_path

def load_job_data():
    """โหลดข้อมูลตำแหน่งงานและทักษะจากไฟล์ JSON"""
    json_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'job_skills_mock.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def analyze_skill_gap(user_skills):
    """เปรียบเทียบทักษะผู้ใช้กับทุกตำแหน่งงาน"""
    job_data = load_job_data()
    result = []

    for job in job_data:
        required = set(job['skills'])
        user = set(user_skills)
        matched = required & user
        missing = required - user
        percent_match = round(len(matched) / len(required) * 100)

        learning_steps = get_learning_path(sorted(missing))

        result.append({
            "role": job['role'],
            "matched_skills": sorted(matched),
            "missing_skills": sorted(missing),
            "match_percent": percent_match,
            "learning_path": learning_steps
        })

    return sorted(result, key=lambda x: x['match_percent'], reverse=True)
