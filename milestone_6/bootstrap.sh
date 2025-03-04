#!/bin/bash

set -e

update_system() {
    echo "Updating system..."
    sudo apt update -y && sudo apt upgrade -y
}

install_packages() {
    echo "Installing required packages..."
    sudo apt install -y docker.io docker-compose make python3-venv
}

start_docker() {
    echo "Starting Docker service..."
    sudo systemctl enable docker
    sudo systemctl start docker
}

configure_user() {
    echo "Adding Vagrant user to Docker group..."
    sudo usermod -aG docker vagrant
}

setup_virtualenv() {
    echo "Activating Python virtual environment..."
    sudo python3 -m venv /vagrant/venv
    . /vagrant/venv/bin/activate
}

install_dependencies() {
    echo "Installing dependencies..."
    pip install -r /vagrant/requirements.txt
}



deploy_application() {
    echo "Deploying application..."
    cd /vagrant/
    sudo make start-api
}

main() {
    update_system
    install_packages
    start_docker
    configure_user
    setup_virtualenv
    install_dependencies
    deploy_application

    echo "Deployment setup completed!"
}

main
