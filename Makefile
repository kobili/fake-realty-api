make-migrations-empty:
	poetry run python manage.py makemigrations ${app_label} --name ${name} --empty
mme: make-migrations-empty

migrate:
	poetry run python manage.py migrate
m: migrate

run-django:
	poetry run python manage.py runserver
run: run-django
