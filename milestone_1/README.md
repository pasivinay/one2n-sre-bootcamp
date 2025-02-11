# Milestone 1 - Student CRUD API

This is a simple CRUD API for managing student records.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/pasivinay/one2n-sre-bootcamp.git
    cd student-crud-api
    ```

2. Install dependencies:
    ```bash
    make install
    ```

3. Set up the database:
    ```bash
    make create-db
    ```

4. Run the app:
    ```bash
    make run
    ```

5. API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- `GET /api/v1/students` - Get all students
- `GET /api/v1/students/<id>` - Get a student by ID
- `POST /api/v1/students` - Add a new student
- `PUT /api/v1/students/<id>` - Update a student's information
- `DELETE /api/v1/students/<id>` - Delete a student
- `GET /api/v1/healthcheck` - Health check

## Postman Collection

You can import the Postman collection from `postman_collection/one2n-sre-bootcamp.postman_collection.json` to test the API.

# Postman Demo

Below are snapshots demonstrating the working of the CRUD API. These images can be found in `./postman_collection/postman_snapshots`.

1. **Get all students** - Initially, the list is empty.
   ![image](./postman_collection/postman_snapshots/1-get-all-students-empty.png)

2. **Get a specific student by ID** - Response shows "student not found".
   ![image](./postman_collection/postman_snapshots/2-get-student-not-found.png)

3. **Add a new student** using `POST` request.
   ![image](./postman_collection/postman_snapshots/3-add-student.png)

4. **Get all students** - Now it shows the added student.
   ![image](./postman_collection/postman_snapshots/4-get-all-students-after-addition.png)

5. **Get a specific student by ID** - Returns the student details.
   ![image](./postman_collection/postman_snapshots/5-get-student-by-id.png)

6. **Add another student**.
   ![image](./postman_collection/postman_snapshots/6-add-another-student.png)

7. **Get all students** - Shows multiple students.
   ![image](./postman_collection/postman_snapshots/7-get-all-students-multiple.png)

8. **Update student details** using `PUT` request.
   ![image](./postman_collection/postman_snapshots/8-update-student.png)

9. **Get updated student details**.
   ![image](./postman_collection/postman_snapshots/9-get-updated-student.png)

10. **Delete a student** using `DELETE` request.
    ![image](./postman_collection/postman_snapshots/10-delete-student.png)

11. **Get all students** - Confirms student deletion.
    ![image](./postman_collection/postman_snapshots/11-get-all-after-delete.png)

12. **Run health check request**.
    ![image](./postman_collection/postman_snapshots/12-healthcheck.png)