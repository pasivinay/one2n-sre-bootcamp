# Stage 1: Builder Stage
FROM python:3.12-alpine AS builder

# Set working directory
WORKDIR /app

# Install application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

