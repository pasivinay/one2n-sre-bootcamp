.PHONY : install run migrate test create-db

install:
	pip install -r requirements.txt

run:
	flask run

migrate:
	flask db init
	flask db migrate
	flask db upgrade

test:
	pytest test_api.py --disable-warnings

create-db:
	python3 create-db.py
