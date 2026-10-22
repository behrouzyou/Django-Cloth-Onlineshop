# Django Cloth Online Shop

A Django-based clothing e-commerce project organized into separate apps for products, orders, blog content, core functionality, and website pages.

## Tech stack
- Python and Django
- Django REST Framework
- SQLite database in the current development configuration
- Jazzmin admin theme
- CKEditor

## Repository layout
- `onlineshop/` — Django project configuration
- `products/` — product app
- `orders/` — order-related app
- `blog/` — blog content
- `core/` and `web/` — shared/site functionality
- `static/` — static assets
- `manage.py` — Django management entry point

## Run locally
Requires Python and pip.

```bash
git clone https://github.com/behrouzyou/Django-Cloth-Onlineshop.git
cd Django-Cloth-Onlineshop
python -m venv .venv
```

Activate the virtual environment, then install the dependencies used by the project. If a requirements file is added, use it to reproduce the exact environment. Create a new development secret key and configure it through an environment variable before running the project.

```bash
python manage.py migrate
python manage.py runserver
```

Open the local URL shown by Django.

## Security and repository hygiene
The current repository includes a SQLite database and development configuration. Do not use committed database contents or development settings in production. Keep local databases, IDE metadata, and secrets out of future commits.
