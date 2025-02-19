# Declaring these targets as phony to indicate they are not actual files
.PHONY: install build run test migrate tag-push lint


# Install all required dependencies from requirements.txt
install:
	pip install -r requirements.txt


# Build docker image for flask api
build: migrate
	sudo docker build -t student-api:$(VERSION) .


# Start flask api container with built image
run:
	sudo docker run --rm -dit -p 5000:5000 --env-file .env student-api:$(VERSION) 


# Run unit tests using pytest
test: install
	pytest app/test_api.py --disable-warnings


# Run DB schema migration on students database
migrate:
	cd app && \
	flask db init && \
	flask db migrate && \
	flask db upgrade


# Tag and push docker image to a repository
tag-push:
	sudo docker tag student-api:$(VERSION) $(USERNAME)/student-api:$(VERSION)
	sudo docker push $(USERNAME)/student-api:$(VERSION)

# Run linting on python files
lint:
	pylint *.py