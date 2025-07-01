# Private Me - Личный дневник на Django

## Описание проекта

PPrivate Me - это веб-приложение для ведения личного дневника, развернутое в Docker-контейнерах. Проект включает три основных сервиса:
- **app** - Django-приложение
- **db** - PostgreSQL база данных
- **nginx** - Веб-сервер
- 
## Основные функции

- 📝 Создание, редактирование и удаление записей
- 🔐 Аутентификация и авторизация пользователей
- 🏷️ Категории и теги для записей
- 🔍 Поиск по содержимому записей
- 📅 Календарь и фильтрация по датам

## Технологии

- 🐍 Python 3.12 + Django 5.2
- 🐘 PostgreSQL
- 🛳️ Docker + Docker Compose
- 🚀 Nginx

### Быстрый старт

### Предварительные требования
- Установленный Docker и Docker Compose

### Запуск приложения
1. Клонируйте репозиторий:
```bash
git clone git@github.com:Genekold/PrivateMe.git
cd PrivateMe
```
2. Создайте файл окружения и внесите в него свои данные:
```bash
cp .env.example .env
```
3 Запустите сервисы и дождитесь запуска всех контейнеров:
```bash
docker-compose up -d
```
4 Создайте суперпользователя:
```bash
docker-compose exec app python manage.py create_super_user
```
## Доступ к приложению
После успешного запуска контейнеров приложение будет доступно:
🔗 [http://localhost](http://localhost)

## Управление сервисами

### Остановка контейнеров
Чтобы остановить все работающие контейнеры проекта:
```bash
docker-compose down
```

### Просмотр логов:
Чтобы остановить все работающие контейнеры проекта:
```bash
docker-compose logs -f
```

## Настройка окружения

Основные переменные окружения настраиваются в файле `.env` в корне проекта:

```ini
# Настройки PostgreSQL
POSTGRES_DB=private_me
POSTGRES_USER=postgres
POSTGRES_PASSWORD=securepassword
DB_HOST=localhost
DB_PORT=5432

# Настройки Django
SECRET_KEY=yoursecretkey
DEBUG=False

# Дополнительные настройки 
EMAIL_HOST_USER=smtp.example.com
EMAIL_HOST_PASSWORD=qwertyuiop
```

<div align="center" style="margin-top: 40px;">

**Private Me** — ваш личный цифровой дневник  
© 2023 | [Политика конфиденциальности](#) | [Условия использования](#)

[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)

</div>