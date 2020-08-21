# Django Python
Django Web Framework (Python)

# Log of Tests

## August, 19 2020

- Implementation of **SiteTest_1** based on [Django Tutorial 01](https://docs.djangoproject.com/en/3.0/intro/tutorial01/) using ngrok to tunnel the server.

- Simple HTML code test.

## August, 20 2020

- Simple CSS code test.
- SQL tests.
- Extension of **models.py** module.

  Example:
  > `from django.db import models`  
  > `class User(models.Model):`  
  >> `name  = models.CharField(max_length=128)`  
  >> `email = models.CharField(max_length=128)`

***

## Configuration
> To run: `python manage.py runserver`  
> To check: `python3 manage.py check`  
> To extend the models: `python3 manage.py makemigrations`  
> To remove database: `rm db.sqlite3`  
> To create database and table(s): `python3 manage.py migrate`  
> To start the Django shell: `python3 manage.py shell`  

***

**Notes:**
- To validate HTML code use
  [Nu Html Checker](https://validator.w3.org/nu)
- To validate CSS code use
  [CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- About Model–View–Controller
  ([MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller))
