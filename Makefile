install_deps: 
	@pip install -r requeriments.txt

migrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

run:
	@python manage.py runserver