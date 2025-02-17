# Declaring these targets as phony to indicate they are not actual files
.PHONY: build run tag-push

# Build docker image for flask api
build:
	sudo docker build -t student-api:$(VERSION) .


# Start flask api container with built image
run:
	sudo docker run --rm -dit -p 5000:5000 --env-file .env student-api:$(VERSION) 

# Run unit tests using pytest
test:
	pytest test_api.py --disable-warnings

# Tag and push docker image to a repository
tag-push:
	sudo docker tag student-api:$(VERSION) <your-dockerhub-username>/student-api:$(VERSION)
	sudo docker push <your-dockerhub-username>/student-api:$(VERSION)
