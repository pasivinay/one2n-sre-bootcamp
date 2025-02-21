# Milestone 3 - Setup one-click local development setup

## Project Description

This project is a simple CRUD API designed for managing student records. The API is built using Python and Flask, following best practices for RESTful API design and the Twelve-Factor App methodology. It provides functionality to create, read, update, and delete student records while ensuring proper API versioning, structured logging, and configuration management using environment variables.

The API is container-ready, follows dependency management practices, and supports database migrations to maintain schema consistency.

## Prerequisites

Before proceeding, ensure you have the following installed on your system:

- Python 3.8+
- pip (Python package manager)
- Docker
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

1. Clone the repository and switch to `milestone_4` branch:
    ```bash
    git clone https://github.com/pasivinay/one2n-sre-bootcamp.git
    cd one2n-sre-bootcamp/milestone_4
    ```

## Automatic Trigger  
The GitHub Actions workflow is automatically triggered when changes are made within the `milestone_4/app` directory. Simply modify any necessary files, commit the changes, and push them to the repository. This will initiate the CI pipeline.

## Manual Trigger  
If needed, you can manually trigger the workflow from the GitHub Actions interface:  
1. Navigate to your repository on GitHub.  
2. Click on the **"Actions"** tab.  
3. Select the workflow named **"CI Pipeline"**.  
4. Click on the **"Run workflow"** button.  
5. Choose the branch (if applicable) and confirm the execution.

## Additional Information  
- The workflow configuration can be found in `.github/workflows/ci-pipeline.yml`.  
- Ensure you have the necessary environment variables and secrets configured in your repository settings (`Settings → Secrets and variables → Actions`).  
- You can monitor workflow progress, view logs, and troubleshoot failures from the **Actions** tab.

For any modifications to the pipeline, update the `.yml` file accordingly and commit the changes.



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
   - Navigate to `milestone_4/postman_collection/one2n-sre-bootcamp.postman_collection.json`
   - Click **Import** in Postman and select this file.

2. Execute API requests:
   - Use the available endpoints to perform CRUD operations.
   - Check the responses to validate the API functionality.

