from flask import Flask
from .models import db
from .routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university_courses.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(api_bp, url_prefix='/api')
    return app