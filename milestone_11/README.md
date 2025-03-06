# Milestone 11 - Configure dashboards & alerts

## Project Description

This project focuses on enhancing system observability by configuring Grafana dashboards and setting up alerts for critical scenarios. The goal is to monitor system performance effectively and receive alerts for anomalies via Slack.

## Prerequisites

Before proceeding, ensure you have the following pre-requisities available and installed on your system:

- Docker
- minikube cluster (Follow milestone 6 to provision required nodes)
- helm
- vault
- argocd
- slack account
- slack webhook url
- milestone 10 setup


## Setup Instructions

1. Clone the repository and switch to `milestone_11` branch:
    ```bash
    git clone https://github.com/pasivinay/one2n-sre-bootcamp.git
    cd one2n-sre-bootcamp/milestone_11
    ```

2. Deploy grafana dashboards:
    ```bash
    kubectl create configmap grafana-dashboard-database -n observability --from-file helm/observability/dashboards/database_metrics.json --from-file helm/observability/dashboards/application_error_logs.json --from-file helm/observability/dashboards/kube-state-metrics.json --from-file helm/observability/dashboards/blackbox-metrics.json --from-file helm/observability/dashboards/node-metrics.json

    kubectl label configmap -n observability grafana-dashboard-database grafana_dashboard="1"
    ```

> **_NOTE:_**  You can configure your slack webhook url and slack channel variables by editing values for `alertmanager.config.global.slack_api_url` and `alertmanager.config.receivers.slack_configs.channel` in `prometheus-values.yaml`.


3. Deploy alerts with notifications sent to slack channel:
    ```bash
    helm upgrade --install prometheus prometheus-community/kube-prometheus-stack -f  helm/observability/prometheus-values.yaml --namespace observability --create-namespace
    ```

4. Access Grafana local instance at `http://127.0.0.1:3000/` by exposing application with :
    ```bash
    export POD_NAME=$(kubectl --namespace observability get pod -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=prometheus" -oname)

    kubectl --namespace observability port-forward $POD_NAME 3000 &
    ```\

5. Open Grafana and navigate to `Dashboards`, then use the search bar to filter dashboards by entering `one2n-sre-bootcamp-dashboards` tag.


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
   - Navigate to `milestone_11/postman_collection/one2n-sre-bootcamp.postman_collection.json`
   - Click **Import** in Postman and select this file.

2. Execute API requests:
   - Use the available endpoints to perform CRUD operations.
   - Check the responses to validate the API functionality.

