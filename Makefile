all: install

install: local migrate loaddata

local:
	pip install -r requirements.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate

loaddata:
	python manage.py loaddata core core.json

run:
	python manage.py runserver