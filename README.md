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
 
### Installation

Clone the repo
```python
$ git clone https://github.com/iyanuashiri/exchange-api.git

$ cd exchange-api
```

Run migrations
```python
$ sudo docker-compose exec web python manage.py makemigrations

$ sudo docker-compose exec web python manage.py migrate
```

Run server
```python
$ python manage.py runserver
```
Application URL
http://localhost:8000/

API Documentation link
http://localhost:8000/swagger/

Available Endpoints

POST http://127.0.0.1:8000/api/v1/auth/users/ - Create Account endpoint

POST http://127.0.0.1:8000/api/v1/auth/token/login/ - Login endpoint

POST http://127.0.0.1:8000/api/v1/quotes/ - Post quotes endpoint

GET http://127.0.0.1:8000/api/v1/quotes/ - List of quotes endpoint 


## Docker

### Run migrations

```python
$ sudo docker-compose exec web python manage.py makemigrations

$ sudo docker-compose exec web python manage.py migrate
```




### Test coverage
To run the tests, check your test coverage, and generate a simplified coverage report:

```python
$ sudo docker-compose exec web pytest -v
```

