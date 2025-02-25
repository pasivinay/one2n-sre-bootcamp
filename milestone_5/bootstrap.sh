#!/bin/bash

set -e

echo "Updating system..."
sudo apt update -y && sudo apt upgrade -y

echo "Installing required packages..."
sudo apt install -y docker.io docker-compose nginx

echo "Starting Docker service..."
sudo systemctl enable docker
sudo systemctl start docker

echo "Adding Vagrant user to Docker group..."
sudo usermod -aG docker vagrant

echo "Deployment setup completed!"
