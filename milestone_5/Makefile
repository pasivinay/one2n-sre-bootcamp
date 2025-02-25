build-api:
	sudo docker build -t myrepo/api:1.0.0 -f Dockerfile .

start-db:
	sudo docker-compose up -d db

run-migrations:
	sudo docker-compose run --rm api1 flask db upgrade

deploy:
	sudo docker-compose up -d

status:
	sudo docker ps
