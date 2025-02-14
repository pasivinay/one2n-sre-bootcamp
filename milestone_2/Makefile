# Declaring these targets as phony to indicate they are not actual files
.PHONY: install run migrate test create-db

# Install all required dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Run the Flask application
run:
	flask run

# Perform database migrations
migrate:
	# Initialize the database migration repository
	flask db init
	# Generate migration scripts based on detected changes in models
	flask db migrate
	# Apply migrations to update the database schema
	flask db upgrade

# Run unit tests using pytest
test:
	pytest test_api.py --disable-warnings

# Create the database using the specified Python script
create-db:
	python3 create-db.py
