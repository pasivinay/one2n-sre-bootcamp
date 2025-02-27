# Milestone 6 - Setup Kubernetes cluster

## Project Description

This setup provisions a three-node Kubernetes cluster using Minikube on your local machine. The cluster will be treated as a production-like environment for deploying applications, databases, and dependent services.

## Cluster Node Configuration

The cluster will consist of three nodes with specific roles:

`Node A`: Dedicated for application deployment.

`Node B`: Hosts the database.

`Node C`: Runs dependent services such as the observability stack and Vault for secret management.

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


1. Clone the repository and switch to `milestone_6` branch:
    ```bash
    git clone https://github.com/pasivinay/one2n-sre-bootcamp.git
    cd one2n-sre-bootcamp/milestone_6
    ```

2. Install Minikube & kubectl
    ```bash
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube

    # Install kubectl
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x kubectl
    sudo mv kubectl /usr/local/bin/
    ```

3. Start a Three-Node Minikube Cluster:
    ```bash
    minikube start --nodes 3 --driver=docker
    ```

4. Label the Nodes:
    ```bash
    kubectl label nodes minikube type=application
    kubectl label nodes minikube-m02 type=database
    kubectl label nodes minikube-m03 type=dependent_services
    ```

5. Verify the label on the nodes with:
    ```bash
    kubectl get nodes -L type
    ```
