from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import logging
from flask_migrate import Migrate
from logging.config import dictConfig

load_dotenv()

dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s",
            },
            "simple": {
                "format": "%(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": "INFO",
            },
            "file_info": {
                "class": "logging.FileHandler",
                "filename": "access.log",
                "formatter": "standard",
                "level": "INFO",
            },
            "file_error": {
                "class": "logging.FileHandler",
                "filename": "error.log",
                "formatter": "detailed",
                "level": "ERROR",
            },
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["console", "file_info"],
                "level": "INFO",
            },
            "app.module": {
                "handlers": ["console", "file_error"],
                "level": "ERROR",
                "propagate": False,
            },
        },
    }
)

access = logging.getLogger("root")
error = logging.getLogger("app.module")

# Set up the app and database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import Student


# Routes
@app.route("/api/v1/students/", methods=["GET"])
def get_students():
    access.info("Fetching all students")
    students = Student.query.all()
    return jsonify([student.as_dict() for student in students])


@app.route("/api/v1/students/<int:id>/", methods=["GET"])
def get_student(id):
    student = Student.query.get(id)
    if student:
        access.info(f"Fetching student with ID {id}")
        return jsonify(student.as_dict())
    error.error(f"Student with ID {id} not found")
    return jsonify({"message": "Student not found"}), 404


@app.route("/api/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = Student(name=data["name"], age=data["age"])
    db.session.add(new_student)
    db.session.commit()
    access.info(f"Added student {new_student.name} with ID {new_student.id}")
    return jsonify(new_student.as_dict()), 201


@app.route("/api/v1/students/<int:id>/", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)
    if student:
        student.name = data["name"]
        student.age = data["age"]
        db.session.commit()
        access.info(f"Updated student with ID {id}")
        return jsonify(student.as_dict())
    error.error(f"Student with ID {id} not found")
    return jsonify({"message": "Student not found"}), 404


@app.route("/api/v1/students/<int:id>/", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        access.info(f"Deleted student with ID {id}")
        return jsonify({"message": "Student deleted"}), 200
    error.error(f"Student with ID {id} not found")
    return jsonify({"message": "Student not found"}), 404


@app.route("/api/v1/healthcheck/", methods=["GET"])
def healthcheck():
    access.info("Healthcheck endpoint hit")
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(debug=True)
