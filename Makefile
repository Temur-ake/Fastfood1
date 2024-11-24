app:
	python3 manage.py startapp apps

run:
	python3 manage.py runserver

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

sup:
	python3 manage.py createsuperuser