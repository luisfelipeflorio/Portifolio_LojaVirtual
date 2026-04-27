# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Projeto

E-commerce de confeitaria artesanal — Django 5.x full stack com TailwindCSS. Interface inteiramente em **português brasileiro**; código em **inglês**.

---

## Comandos

### Setup inicial

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # preencher SECRET_KEY
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### TailwindCSS (rodar em paralelo com o servidor)

```bash
# desenvolvimento
tailwindcss -i static/src/input.css -o static/css/output.css --watch

# produção
tailwindcss -i static/src/input.css -o static/css/output.css --minify
```

### Migrations

```bash
python manage.py makemigrations <app>
python manage.py migrate
```

### Testes (Sprint 7 em diante)

```bash
python manage.py test <app>
python manage.py test <app>.tests.TestClassName.test_method_name
```

---

## Arquitetura

Seis apps Django com responsabilidades bem separadas:

| App | Responsabilidade |
|---|---|
| `core` | Home, páginas estáticas, `TimeStampedModel`, context processor global |
| `catalog` | Models `Category` e `Product`; views de listagem, filtro e detalhe |
| `cart` | Classe `Cart` em `cart/cart.py`; carrinho mantido na sessão Django |
| `orders` | Models `Order` e `OrderItem`; checkout, histórico, e-mails via signals |
| `accounts` | `CustomUser` (AbstractUser), `Address`; registro, login, perfil |
| `dashboard` | Painel restrito a `is_staff`; CRUD de produtos/categorias e gestão de pedidos |

### Fluxo principal

```
Catálogo → Carrinho (sessão) → Checkout (Form) → Order + OrderItems → E-mail (signal)
```

### Padrões transversais

- **`TimeStampedModel`** (`core/models.py`): model abstrato com `created_at` e `updated_at` — todo model herda dele.
- **`StaffRequiredMixin`** (`dashboard/mixins.py`): aplica `LoginRequiredMixin` + verifica `is_staff`; usado em todas as views do `dashboard`.
- **Cart context processor** (`cart/context_processors.py`): injeta `cart_count` em todos os templates via `TEMPLATES[0]['OPTIONS']['context_processors']`.
- **Signals em `signals.py`**: e-mails de confirmação e atualização de status são disparados por signals em `orders/signals.py`, conectados no `orders/apps.py` via `ready()`.

---

## Convenções de Código

- **PEP 8**; **aspas simples** em todo o Python.
- **CBVs** preferencialmente (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `FormView`, `TemplateView`, `View`).
- Slugs auto-gerados via `slugify` no `save()` do model.
- Formulários estilizados via `attrs` no `__init__` ou `django-widget-tweaks` nos templates.
- Templates estendem `base.html`; partials reutilizáveis têm prefixo `_` (ex: `_product_card.html`).
- Sem frameworks JS externos — JS vanilla quando necessário.
- Namespaces de URL definidos com `app_name` em cada `urls.py`.

---

## Variáveis de Ambiente

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Em desenvolvimento, e-mails são impressos no console:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

## Documentação

Consultar `docs/` para referências detalhadas:

- `docs/architecture.md` — stack, estrutura de diretórios, configurações de settings
- `docs/data-models.md` — schema completo dos models e suas relações
- `docs/code-guidelines.md` — convenções, padrões de views, signals e templates
- `docs/design-system.md` — paleta, tipografia, gradientes e componentes TailwindCSS
