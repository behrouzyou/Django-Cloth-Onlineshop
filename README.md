# Django Cloth Online Shop

A Django clothing e-commerce project organized into apps for products, orders, blog content, core functionality, and website pages.

## Stack
- Python and Django
- Django REST Framework
- SQLite in the current development configuration
- Jazzmin admin theme
- CKEditor

## Structure
- `onlineshop/` — project configuration
- `products/`, `orders/`, `blog/` — application modules
- `core/`, `web/` — shared/site functionality
- `static/` — static assets
- `manage.py` — Django management entry point

## Run locally
Create and activate a virtual environment, install the project's dependencies, then run:

```bash
python manage.py migrate
python manage.py runserver
```

Configure a development secret key before running. The repository does not currently include a requirements file, so install dependencies based on the project's imports or add a pinned dependency list.

## Security and repository hygiene
Do not use committed database contents or development settings in production. Keep local databases, IDE metadata, and secrets out of future commits.
