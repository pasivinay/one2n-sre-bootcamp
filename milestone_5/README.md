# Milestone 5 - Deploy REST API & its dependent services on bare metal

## Project Description

This project focuses on deploying a REST API and its dependent services using Vagrant as the production environment. The deployment is automated using docker-compose and Makefile, ensuring a seamless setup.

## Prerequisites

Before proceeding, ensure you have the following installed on your system:

- Python 3.8+
- pip (Python package manager)
- Docker
- Vagrant
- Oracle VirtualBox
- Dockerhub account
- Docker logged in with dockerhub account
- Virtualenv (Recommended for managing dependencies)
- Make (for executing build and run commands)
- PostgreSQL or SQLite (for database)

## Requirements File (`requirements.txt`)

The project dependencies are managed through `requirements.txt`. Below is the content of this file:

```
Flask==3.1.0
Flask-Migrate==4.1.0
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.1
pytest==8.3.4
PyMySQL==1.1.1

```

## Setup Instructions

> **_NOTE:_**  Please configure your environment variables(`.env`) file before building the docker image. An example `.env` file is provided as `.example.env`. Copy the example file to `.env` file and modify as required.

1. Clone the repository and switch to `milestone_5` branch:
    ```bash
    git clone https://github.com/pasivinay/one2n-sre-bootcamp.git
    cd one2n-sre-bootcamp/milestone_5
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    make install
    ```
4. Run unit tests on application:
    ```bash
    make test
    ```
5. Run database migration initialization:
    ```bash
    make migrate
    ```

6. Start the Vagrant VM:
    ```bash
    vagrant up
    ```

7. Provision the VM to start the api server:
    ```bash
    vagrant provision
    ```

8. For troubleshooting, connect to the vm with:
    ```bash
    vagrant ssh
    ```

9. Clear the vagrant box with:
    ```bash
    vagrant destroy
    ```

10. The API will be available at `http://127.0.0.1:8080/`.


## API Endpoints

### 1. Get all students
- **Endpoint:** `GET /api/v1/students`
- **Description:** Fetches all student records from the database.

### 2. Get a student by ID
- **Endpoint:** `GET /api/v1/students/<id>`
- **Description:** Retrieves details of a specific student by their unique ID.

### 3. Add a new student
- **Endpoint:** `POST /api/v1/students`
- **Description:** Adds a new student to the database.
- **Request Body (JSON Example):**
    ```json
    {
        "name": "John Doe",
        "age": 21
    }
    ```

### 4. Update student details
- **Endpoint:** `PUT /api/v1/students/<id>`
- **Description:** Updates the details of an existing student.
- **Request Body (JSON Example):**
    ```json
    {
        "name": "John Updated",
        "age": 22
    }
    ```

### 5. Delete a student
- **Endpoint:** `DELETE /api/v1/students/<id>`
- **Description:** Deletes a student record from the database.

### 6. Health check
- **Endpoint:** `GET /api/v1/healthcheck`
- **Description:** Checks if the API is running properly.


## Using Postman for API Testing

1. Open Postman and import the collection file:
   - Navigate to `milestone_5/postman_collection/one2n-sre-bootcamp.postman_collection.json`
   - Click **Import** in Postman and select this file.

2. Execute API requests:
   - Use the available endpoints to perform CRUD operations.
   - Check the responses to validate the API functionality.

