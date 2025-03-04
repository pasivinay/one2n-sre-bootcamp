# Milestone 9 - Setup one-click deployments using ArgoCD

## Project Description

This project integrates GitOps principles using ArgoCD for automated deployments. ArgoCD will manage deployments based on changes merged into the GitHub repository, ensuring continuous synchronization with the Kubernetes cluster.

## Prerequisites

Before proceeding, ensure you have the following installed on your system:

- Docker
- minikube cluster (Follow milestone 6 to provision required nodes)
- helm
- vault
- argocd


## Setup Instructions

1. Clone the repository and switch to `milestone_9` branch:
    ```bash
    git clone https://github.com/pasivinay/one2n-sre-bootcamp.git
    cd one2n-sre-bootcamp/milestone_9
    ```

2. Deploy Namespaces:
    ```bash
    helm install namespaces helm/namespaces
    ```

3. Provision the vault server form helm chart for vault:
    ```bash
    helm install vault helm/vault -n vault
    ```
***
   #### Steps to Set Up Vault and Initialize secrets:

1. Port-forward Vault Service and set VAULT_ADDR env.

    To access Vault locally, port-forward the service to port `8200` and export VAULT_ADDR:

    ```bash
    kubectl port-forward svc/vault -n vault 8200:8200 &

    export VAULT_ADDR=http://127.0.0.1:8200
    ```

2. Initialize Vault

    Run the following command to initialize Vault and generate unseal keys:

    ```bash
    vault operator init -key-shares=1 -key-threshold=1 -format=json
    ```

This will return an unseal key and a root token.

3. Unseal Vault

    Use the unseal key from the previous command to unseal Vault:

    ```bash
    vault operator unseal <unseal_key>
    ```

4. Login with Root Token

    Use the root token from the initialization step to authenticate:

    ```bash
    vault login <root_token>
    ```

5. Enable Secret Engine

    Enable a KV secrets engine at path `db-creds`:

    ```bash
    vault secrets enable -path=secret kv-v2
    ```

6. Add Secrets to Vault

    Add required secrets to `db-creds`:

    ```bash
    vault kv put secret/db-creds username=<db_user> password=<db_password> database=<db_name> root-password=<root_password> db-url=<database_url>
    ```

    **Note:** Replace `<db_user>`, `<db_password>`, `<db_name>`, `<root_password>`, and `<database_url>` with actual values.

7. Verify Secrets

    Confirm that the secrets have been added successfully:

    ```bash
    vault kv get secret/db-creds
    ```
***

4. Deploy Vault Root Token into Kubernetes Secrets:

    ```bash
    kubectl create secret generic vault-token --from-literal=token=<root-token> -n external-secrets
    ```

5. Install helm chart for ArgoCD:
    ```bash
    helm repo add argo https://argoproj.github.io/argo-helm

    $ helm install argocd argo/argo-cd --namespace argocd --create-namespace -f helm/argocd/values.yaml
    ```


6. Fetch inital admin secret for argocd containing initial login password:
    ```bash
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
    ```

7. Port-forward argocd service to access the dashboard from host and login with the username:admin and password retrived from above step:
    ```bash
    kubectl port-forward service/argocd-server -n argocd 8081:443 &
    ```

8. Install helm chart for external-secret:
    ```bash
    helm repo add external-secrets https://charts.external-secrets.io
    
    helm install external-secrets external-secrets/external-secrets -n external-secrets
    ```

9. Deploy Application components with ArgoCD helm chart :

    ```bash
    helm install argocd-student-api helm/argocd -n student-api
    ```

10. Expose Application Service on Localhost:

    ```bash
    kubectl -n student-api port-forward services/student-api 8080:5000 &
    ```

11. The API will be available at `http://127.0.0.1:8080/`.

12. Update the image tag by editing the pipeline file or manually triggering pipeline and passing the image tag as input from main branch.

13. Verify the updated image from ArgoCD Dashboard accessible at `http://127.0.0.1:8081/`.



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
   - Navigate to `milestone_9/postman_collection/one2n-sre-bootcamp.postman_collection.json`
   - Click **Import** in Postman and select this file.

2. Execute API requests:
   - Use the available endpoints to perform CRUD operations.
   - Check the responses to validate the API functionality.

