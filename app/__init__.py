from flask import Flask
from flask_session import Session
from app import routes
import os

def create_app():
    app = Flask(__name__)

    # ตั้งค่า Session (ใช้ filesystem เก็บ)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    from .routes import main
    app.register_blueprint(main)

    return app