# Planetary Play
## A Small Code Interview Django App

## N.B.
The relevant code for the completed task is in the root-level app "planetary play". This is by design to make
the separation clear.

As the starting point API appears to only have moons orbiting planets these
are the only bodies that are uploaded currently. This could be easily changed in the
upload script.

The DEBUG option is still turned on as the assumption is that the code will be run locally. This
could also be easily changed in the settings.py file.

## Getting started
Quickstart:
```
python -m venv py_env

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runscript upload

python manage.py runserver
```

## Quick Exploration of the API
There is a set of convenience functions to use in /tests. You can
use these to test the basic functionality of the API and explore the endpoints.
