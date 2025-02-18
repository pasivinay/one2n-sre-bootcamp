# Stage 1: Builder Stage
FROM python:3.12-alpine AS builder

# Set working directory
WORKDIR /app

# Install application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY ./app .

# Stage 2: Runtime Stage
FROM python:3.12-alpine

# Set working directory
WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

# Expose the API port
EXPOSE 5000

# Create Database Instance
RUN python3 /app/create-db.py

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the application
CMD ["flask", "run"]