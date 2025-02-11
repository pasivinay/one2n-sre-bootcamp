from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import logging
from flask_migrate import Migrate

# Set up the app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Models
from models import Student

# Routes
@app.route('/api/v1/students/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.as_dict() for student in students])

@app.route('/api/v1/students/<int:id>/', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if student:
        return jsonify(student.as_dict())
    return jsonify({"message": "Student not found"}), 404

@app.route('/api/v1/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.as_dict()), 201

@app.route('/api/v1/students/<int:id>/', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)
    if student:
        student.name = data['name']
        student.age = data['age']
        db.session.commit()
        return jsonify(student.as_dict())
    return jsonify({"message": "Student not found"}), 404

@app.route('/api/v1/students/<int:id>/', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted"}), 200
    return jsonify({"message": "Student not found"}), 404

@app.route('/api/v1/healthcheck/', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)
