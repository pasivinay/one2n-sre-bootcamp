# Milestone 10 - Setup an observability stack

## Project Description

This project sets up a PLG (Promtail, Loki, Grafana) stack along with Prometheus to enhance system observability. It enables monitoring of applications, dependent services, and key system metrics such as DB performance, endpoint latency, and uptime.

## Prerequisites

Before proceeding, ensure you have the following pre-requisities available and installed on your system:

- Docker
- minikube cluster (Follow milestone 6 to provision required nodes)
- helm
- vault
- argocd
- milestone 9 setup


## Setup Instructions

1. Clone the repository and switch to `milestone_10` branch:
    ```bash
    git clone https://github.com/pasivinay/one2n-sre-bootcamp.git
    cd one2n-sre-bootcamp/milestone_10
    ```

2. Install prometheus community helm chart:
    ```bash
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts 

    helm install prometheus prometheus-community/kube-prometheus-stack \ 
    -f helm/observability/prometheus-values.yml --namespace observability \
    --create-namespace --set nodeSelector.type=dependent_services
    ```

3. Get Grafana 'admin' user password by running:
    ```bash
    kubectl --namespace observability get secrets prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo
    ```

4. Access Grafana local instance:
    ```bash
    export POD_NAME=$(kubectl --namespace observability get pod -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=prometheus" -oname)

    kubectl --namespace observability port-forward $POD_NAME 3000 &
    ```

5. Install loki and promtail stack:
    ```bash
    helm repo add grafana https://grafana.github.io/helm-charts
    helm repo update

    helm install loki grafana/loki-stack -f  helm/observability/loki-values.yaml --namespace observability --set nodeSelector.type=dependent_services
    ```

6. Install MySql exporter:
    ```bash
    helm install mysql-exporter prometheus-community/prometheus-mysql-exporter -f helm/observability/ mysql-exported-values.yaml --namespace student-api
    ```

7. Install blackbox exporter exporter:
    ```bash
    helm install blackbox-exporter prometheus-community/prometheus-blackbox-exporter -f helm/observability/blackbox-exporter.yaml --namespace observability
    ```

8. Access grafana dashboard from host at `http://127.0.0.1:3000/` . Login with admin user and password retrieved at step 3.



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
   - Navigate to `milestone_10/postman_collection/one2n-sre-bootcamp.postman_collection.json`
   - Click **Import** in Postman and select this file.

2. Execute API requests:
   - Use the available endpoints to perform CRUD operations.
   - Check the responses to validate the API functionality.

