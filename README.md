#### Тестовое задание для Picasso
Первый запуск:
### 1. docker-compose build
### 2. python test/manage.py makemigrations
### 3. python test/manage.py migrate
### 4. docker-compose up
Последующие запуски:
### 1. docker-compose up

эндпоинт upload/, принимает POST-запросы для загрузки файлов

эндпоинт files/, который будет возвращать список всех файлов, включая статус обработки

на 5555 порту находится Celery Flower для отслеживания tasks