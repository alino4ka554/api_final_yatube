# Yatube API

**Yatube API** — это RESTful API для социальной сети Yatube, позволяющий пользователям публиковать посты, комментировать записи, подписываться на авторов и управлять подписками.

---

## Как запустить проект

### Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone https://github.com/...
cd ... 
```
### Создать и активировать виртуальное окружение:
```sh
python3 -m venv env
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate     # для Windows
```
## Установить зависимости из файла requirements.txt:
```sh
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
### Выполнить миграции:
```sh
python3 manage.py migrate
```
### Запустить проект:
```sh
python3 manage.py runserver
```

## Примеры API-запросов

### Регистрация нового пользователя и получение токена  
**POST** `/api/v1/token/`
```json
{
    "username": "leo",
    "password": "mypassword"
}
```
**Ответ:**
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```
---
### Получение списка всех постов  
**GET** `/api/v1/posts/`
```sh
curl -X GET http://127.0.0.1:8000/api/v1/posts/
```
**Ответ:**
```json
{
    "count": 2,
    "response": [
        {
            "id": 1,
            "text": "Привет, это мой первый пост!",
            "author": "leo",
            "pub_date": "2025-03-26T12:00:00Z"
        }
    ]
}
```
