migrate:										## 🚚 - Remote into local cms container and run python makemigrations migrate
	docker-compose exec cms bash -c 'python3 manage.py makemigrations'
	docker-compose exec cms bash -c 'python3 manage.py migrate'

start:											## 🆙 - Start up the application using Docker compose
	@echo "🆙 - Starting up the application using Docker compose"
	docker-compose up

stop:											## 🛑 - Stop all running containers
	@echo "🛑 - Stopping all running containers"
	docker-compose stop

terminal:										## 🎛  - Remote into local cms container
	docker-compose exec cms /bin/sh
