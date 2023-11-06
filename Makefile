make-migrations-empty:
	python manage.py makemigrations ${app_label} --name ${name} --empty
mme: make-migrations-empty

migrate:
	python manage.py migrate
m: migrate

run-django:
	python manage.py runserver
run: run-django
