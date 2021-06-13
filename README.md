# exchange-api


Exchange API is an app for managing BTC/USD exchange rate from Alphavantage. 

This project has two basic apps.

* accounts - User authentication.
  - Create an Account
  - Get Token
* exchanges
  - GET quotes
  - POST quotes
  

# Technology Stack

  * Python 3.8x
  * Django Web Framework 3.2.4 and Django REST Framework
  * PostgreSQL
 
## Installation

Clone the repo
```python
$ git clone https://github.com/iyanuashiri/exchange-api.git

$ cd exchange-api

$ source venv/bin/activate
```

## How to Setup 

- Click here to get [ALPHAVANTAGE API_KEY](https://www.alphavantage.co/support/#api-key)
- Change `.env_example` to `.env`
- Add your `ALPHAVANTAGE_ACCESS_KEY` into your `.env` file


## Docker

### Run migrations

```python
$ sudo docker-compose exec web python manage.py makemigrations

$ sudo docker-compose exec web python manage.py migrate
```

### Run docker
```python
$ sudo docker-compose up -d

$ sudo docker-compose exec web python manage.py runserver

```

### Test coverage
To run the tests:

```python
$ sudo docker-compose exec web pytest -v
```



Application URL
http://localhost:8000/

API Documentation link
http://localhost:8000/swagger/

Available Endpoints

POST http://127.0.0.1:8000/api/v1/auth/users/ - Create Account endpoint

```python
curl --location --request POST 'http://127.0.0.1:8000/api/v1/auth/users/' \
--form 'email="{{EMAIL_ADDRESS}}"' \
--form 'password="{{PASSWORD}}"'
```


POST http://127.0.0.1:8000/api/v1/auth/token/login/ - Login endpoint

```python
curl --location --request POST 'http://127.0.0.1:8000/api/v1/auth/token/login/' \
--form 'email="{{EMAIL_ADDRESS}}"' \
--form 'password="{{PASSWORD}}"'

```


POST http://127.0.0.1:8000/api/v1/quotes/ - Post quotes endpoint

```python
curl --location --request POST 'http://127.0.0.1:8000/api/v1/quotes/' \
--header 'Authorization: Token {{API_KEY}}' \
```


GET http://127.0.0.1:8000/api/v1/quotes/ - List of quotes endpoint 

```python
curl --location --request GET 'http://127.0.0.1:8000/api/v1/quotes/' \
--header 'Authorization: Token {{API_KEY}}' \
```


