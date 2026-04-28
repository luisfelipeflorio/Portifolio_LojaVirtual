# Confeitaria Virtual

E-commerce de confeitaria artesanal feito com Django 5.x e TailwindCSS.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
```

## Desenvolvimento

Terminal 1:
```bash
python manage.py runserver
```

Terminal 2:
```bash
tailwindcss -i static/src/input.css -o static/css/output.css --watch
```

## Build de Produção

```bash
tailwindcss -i static/src/input.css -o static/css/output.css --minify
python manage.py collectstatic
```

## Estrutura

- `core/` - Home, páginas estáticas
- `catalog/` - Catálogo de produtos
- `cart/` - Carrinho de compras
- `orders/` - Pedidos e checkout
- `accounts/` - Autenticação e perfil
- `dashboard/` - Painel administrativo

## Configuração

Edite o arquivo `.env` com as variáveis de ambiente:

```
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_ENVIRONMENT=development  # ou 'production'
```
