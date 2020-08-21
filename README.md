# Log of Tests with Django
Django Web Framework in Python

## August, 19 2020

- Implementation of **SiteTest_1** based on
  [Django Tutorial 01](https://docs.djangoproject.com/en/3.0/intro/tutorial01/).

- Simple HTML code test.

## August, 20 2020

- Simple CSS code test.
- SQL tests.
- Extension of **models.py** module.

  <pre><code>
  from django.db import models
  class User(models.Model):
      name  = models.CharField(max_length=128)
      email = models.CharField(max_length=128)
                       ...</code></pre>

  **Usage:**

  Start the Django shell with  
  `python3 manage.py shell`  
  <pre><code>
  >>> from usermodel.models import Users  
  >>> u = User(name='Domingo', email='dngallar@iowlabs.com')  
  >>> u.save()  
  >>> print(u.id) # SQL key
  </code></pre>

- Implementation of **SiteTest_2** based on
  [Django Tutorial 02](https://docs.djangoproject.com/en/3.0/intro/tutorial02/).

- **Important:** Modify in `mysite/settings.py`  
  `ALLOWED_HOSTS = []` to `ALLOWED_HOSTS = [ '*' ]`
***

## Creating a project
In shell
> To create a empty project: `django-admin startproject mysite`  
> To run: `python manage.py runserver`  
> To change the port: `python manage.py runserver 8080`  
> To check: `python3 manage.py check`  
> To extend the models: `python3 manage.py makemigrations`  
> To remove database: `rm db.sqlite3`  
> To create database and table(s): `python3 manage.py migrate`  
> To start the Django shell: `python3 manage.py shell`  

### Typical structure

- To create a app: `python manage.py startapp app`
- Modify `app/views.py`
- Create `app/urls.py`
- Modify `mysite/urls.py` with `django.urls.include` and  
  insert into *urlpatterns*: `path('app/', include('app.urls'))`
- Make the app modifiable in the admin.  
  Modify `app/admin.py`

## Model changes

- Change models in `mysite/models.py`
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database

***

**Notes:**
- For online testing (outside **localhost**), **ngrok** is used to tunnel
  to the server.  
  `ngrok http 8000`
- To control HTML `request.GET` use  
  `from django.utils.html import escape`  
  `... escape(request.GET['entry'] ...`  
  Where the url is: `https://domain.com/app?
  <strong>entry=%3Cb%3EExample%3C%2Fb%3E</strong>`
- To validate HTML code use
  [Nu Html Checker](https://validator.w3.org/nu)
- To validate CSS code use
  [CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- About Model–View–Controller
  ([MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller))
