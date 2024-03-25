from flask import Blueprint, jsonify, request
from .models import db, Student, Course, Enrollment

api_bp = Blueprint('api', __name__)

@api_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name} for student in students])

@api_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    student = Student.query.get_or_404(student_id)
    courses = [enrollment.course for enrollment in student.enrollments]
    return jsonify([{'id': course.id, 'name': course.name, 'code': course.code, 'description': course.description} for course in courses])

@api_bp.route('/api/students', methods=['POST'])
def create_student():
    data = request.json
    new_student = Student(first_name=data['first_name'], last_name=data['last_name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created successfully', 'id': new_student.id}), 201

@api_bp.route('/api/courses', methods=['POST'])
def create_course():
    data = request.json
    new_course = Course(name=data['name'], description=data['description'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully', 'id': new_course.id}), 201