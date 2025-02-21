
# Declaring these targets as phony to indicate they are not actual files
.PHONY: install test lint start-db migrate-db build-api start-api setup stop clean

# Install all required dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Run unit tests using pytest
test: install
	pytest app/test_api.py --disable-warnings

set-env:
	python3 -m venv venv
	. venv/bin/activate

# Run linting on python files
lint:
	pylint -E ./app/*.py

# Start the MySQL Database container
start-db:
	@if [ -z "$$(docker ps -q -f name=student-db)" ]; then \
		echo "Starting database container..."; \
		sudo docker compose up -d db; \
		sleep 15  # Wait for DB to be ready; \
	else \
		echo "Database container is already running."; \
	fi

# Run DB schema migration only if not already applied
init-db:
	@if [ -d "app/migrations" ]; then \
		echo "Database migration repository already initialized, skipping..."; \
	else \
		echo "Applying migrations..."; \
		cd app && flask db init; \
	fi

migrate-db:
	@if cd app && flask db check; then \
	    echo "Migrations are already applied."; \
	else \
	    echo "Applying migrations..."; \
	    flask db migrate && flask db upgrade; \
	fi

# Build the API Docker image
build-api: install
	docker build -t student-api:$(VERSION) .

# Start the API container
start-api:
	sudo docker compose up --build -d api
	sudo docker compose exec api flask db upgrade

# One-click setup: Start DB, apply migrations, then start API
setup:
	make start-db
	make init-db
	make migrate-db
	make build-api
	make start-api

# Stop all containers
stop:
	sudo docker compose down

# Remove all containers, volumes, and networks
clean:
	sudo docker compose down -v
	sudo rm -rf ./app/__pycache__ ./app/.pytest_cache
	# sudo rm -rf ./app/migrations ./app/instance mysql_data