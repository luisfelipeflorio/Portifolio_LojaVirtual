# OPENCODE.md

This file provides guidance to Claude Code when working with code in this repository.

---

## Project

E-commerce de confeitaria artesanal — Django 5.x full stack com TailwindCSS. Interface inteiramente em **português brasileiro**; código em **inglês**.

---

## Commands

### Initial Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env         # Fill SECRET_KEY
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### TailwindCSS (run parallel with server)

```bash
# development
tailwindcss -i static/src/input.css -o static/css/output.css --watch

# production
tailwindcss -i static/src/input.css -o static/css/output.css --minify
```

### Migrations

```bash
python manage.py makemigrations <app>
python manage.py migrate
```

---

## Architecture

Six Django apps with well-separated responsibilities:

| App | Responsibility |
|---|---|
| `core` | Home, static pages, `TimeStampedModel`, global context processor |
| `catalog` | `Category` and `Product` models; listing, filter and detail views |
| `cart` | `Cart` class in `cart/cart.py`; cart maintained in Django session |
| `orders` | `Order` and `OrderItem` models; checkout, history, e-mails via signals |
| `accounts` | `CustomUser` (AbstractUser), `Address`; registration, login, profile |
| `dashboard` | Staff-only panel; CRUD for products/categories and order management |

### Main Flow

```
Catalog → Cart (session) → Checkout (Form) → Order + OrderItems → E-mail (signal)
```

### Cross-cutting Patterns

- **`TimeStampedModel`** (`core/models.py`): abstract model with `created_at` and `updated_at` — every model inherits from it.
- **`StaffRequiredMixin`** (`dashboard/mixins.py`): applies `LoginRequiredMixin` + checks `is_staff`; used in all dashboard views.
- **Cart context processor** (`cart/context_processors.py`): injects `cart_count` into all templates via `TEMPLATES[0]['OPTIONS']['context_processors']`.
- **Signals in `signals.py`**: confirmation and status update e-mails are triggered by signals in `orders/signals.py`, connected in `orders/apps.py` via `ready()`.

---

## Code Conventions

- **PEP 8**; **single quotes** everywhere in Python.
- **CBVs** preferably (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `FormView`, `TemplateView`, `View`).
- Slugs auto-generated via `slugify` in model's `save()`.
- Forms styled via `attrs` in `__init__` or `django-widget-tweaks` in templates.
- Templates extend `base.html`; reusable partials have `_` prefix (ex: `_product_card.html`).
- No external JS frameworks — vanilla JS when necessary.
- URL namespace defined with `app_name` in each `urls.py`.

---

## Environment Variables

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

In development, e-mails are printed to console:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

## Documentation

Consult `docs/` for detailed references:

- `docs/architecture.md` — stack, directory structure, settings configuration
- `docs/data-models.md` — complete schema of models and their relationships
- `docs/code-guidelines.md` — conventions, view patterns, signals and templates
- `docs/design-system.md` — palette, typography, gradients and TailwindCSS components