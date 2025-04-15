## Django Backend for Seasons app

This server is a personnal project allowing you to retrieve all the seasonal information for fruits and vegetables based on all the months of the year.
It is an API backend built with Django REST Framework and documented with OpenAPI (Swagger).

## Setup the server for local development

You'll find here all the instructions if you want to run the server locally on your machine :

### Clone the repository

```bash
git clone git@github.com:timonicolaux/seasons-backend.git
cd seasons-backend
```

### Create local virtual environnement and install django

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Apply migrations

```bash
cd project
python manage.py makemigrations
python manage.py migrate
```

### Load data for the project

```bash
python manage.py loaddata data.json
```

### Run the server

```bash
python manage.py runserver
```

### Create a superuser to add/change/delete data (optional)

```bash
python manage.py createsuperuser
```

Then visit http://localhost:8000/admin

### Update data.json file

If you make changes and want to regenerate the data.json file :

```bash
python manage.py dumpdata > data.json
```

### API documentation

Visit the Swagger UI at:
http://localhost:8000/docs

Or access the raw OpenAPI spec:
http://localhost:8000/schema
