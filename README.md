# Django

Use the `uv` library for faster package management and virtual environment setup than traditional `pip` method.

Install uv in linux based systems using : `curl -LsSf https://astral.sh/uv/install.sh | sh`

Create a venv using : `uv venv`

Activate the venve using : `source .venv/bin/activate`

To Decativate use : `deactivate`

Install Django as follows : `uv pip install Django`

Create a Django project (example) : `django-admin startproject mysite djangotutorial`

Run a dev server : `python manage.py runserver`

If default port (8000) is busy : `python manage.py runserver 8001`