# How to setup a virtual environment

## For activating a python environment

```powershell
.\venv\Scripts\Activate
```

## For starting a Django app

```powershell
python manage.py runserver
```

## Updating the database

1. Change your models (in models.py).

2. To create migrations for the changes run:

```
python manage.py makemigrations
```

3. To apply the changes to the database , run:

```
python manage.py migrate
```

## Python Shell

```
python manage.py shell
```

### 🔍 What makes it special?

A normal Python shell - ❌ Doesn’t know anything about your Django project

But "python manage.py shell" - ✅ automatically loads your project settings, connects to your database and lets you import your models directly
