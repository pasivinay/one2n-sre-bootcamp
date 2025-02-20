# Stage 1: Builder Stage
FROM python:3.12-alpine AS builder

# Set working directory
WORKDIR /app


# Create user and set ownership and permissions as required
RUN adduser -D flask && chown -R flask /app

# Install application dependencies
COPY --chown=flask requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=flask ./app .


# Stage 2: Runtime Stage
FROM builder

# Expose the API port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set user as flask
USER flask

# Start the application
ENTRYPOINT ["flask", "run"]