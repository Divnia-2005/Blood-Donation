# Blood Donation

A Django web application for managing blood donation users and blood requests.

## Project structure

- `blooddonation/` - Django project settings and configuration
- `bloodapp/` - main application with models, views, URLs, and migrations
- `templates/` - HTML templates for login, registration, admin and user views
- `static/` - static assets such as images

## Requirements

- Python 3.x
- Django 3.0
- MySQL database

## Database

The project uses MySQL with the following configuration in `blooddonation/settings.py`:

- name: `blood_donation`
- user: `root`
- password: `root`

Update the database settings to match your local environment before running.

## Setup

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install Django and any required packages:

```bash
pip install django mysqlclient
```

3. Create the MySQL database and update `blooddonation/settings.py` if needed.

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Notes

- `DEBUG` is currently set to `True` in `blooddonation/settings.py`; change this for production.
- CSRF middleware is commented out in `settings.py`, so enable it if you harden the application.
- Add allowed hosts in `ALLOWED_HOSTS` if deploying.

## Templates

- `index.html` - likely the app landing page
- `login.html` - login page template
- `adminmodule/adminhome.html` - admin dashboard
- `users/user_register.html` - registration page
- `users/userhome.html` - user dashboard

## Migrations

Database schema changes are stored in `bloodapp/migrations/`.

---

This README provides a quick start for running the Blood Donation application locally.
