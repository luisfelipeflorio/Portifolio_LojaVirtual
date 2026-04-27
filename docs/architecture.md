# Arquitetura Técnica

## Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12 |
| Framework | Django 5.x |
| Banco de dados | SQLite (`django.db.backends.sqlite3`) |
| Frontend | Django Template Language + TailwindCSS 3.x (CLI standalone) |
| E-mail | `django.core.mail.send_mail` via SMTP configurável |
| Mídia | `ImageField` / `FileField` com `MEDIA_ROOT` local |
| Variáveis de ambiente | `python-decouple` + arquivo `.env` |
| Dependências extras | `Pillow`, `django-widget-tweaks` |

---

## Estrutura de Apps

```
confeitaria/           ← projeto Django (settings, urls, wsgi)
├── core/              ← home, páginas estáticas, context processor global
├── catalog/           ← categorias e produtos
├── cart/              ← carrinho via sessão Django
├── orders/            ← pedidos, itens de pedido, status
├── accounts/          ← cadastro, login, perfil, endereços
└── dashboard/         ← painel administrativo customizado
```

Cada app tem seu próprio `urls.py`, incluído no `urls.py` do projeto com prefixo adequado.

---

## Estrutura de Diretórios

```
.
├── confeitaria/           ← configurações do projeto
├── core/
├── catalog/
├── cart/
├── orders/
├── accounts/
├── dashboard/
├── templates/             ← todos os templates HTML
│   ├── base.html
│   ├── _messages.html
│   ├── core/
│   ├── accounts/
│   ├── catalog/
│   ├── cart/
│   ├── orders/
│   │   └── email/         ← templates de e-mail (html + txt)
│   └── dashboard/
├── static/
│   ├── src/
│   │   └── input.css      ← diretivas @tailwind
│   └── css/
│       └── output.css     ← CSS compilado (gerado pelo CLI)
├── media/                 ← uploads (não versionado)
├── manage.py
├── requirements.txt
├── tailwind.config.js
└── .env                   ← não versionado
```

---

## Configuração de Ambiente

Variáveis obrigatórias no `.env`:

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Configurações relevantes em `settings.py`:

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_REDIRECT_URL = 'core:home'
SESSION_COOKIE_AGE = 604800  # 7 dias
```

Em desenvolvimento:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

## TailwindCSS

O projeto usa o **CLI standalone** do TailwindCSS (não CDN).

- `tailwind.config.js` aponta `content` para `templates/**/*.html`
- Compilar em desenvolvimento:
  ```
  tailwindcss -i static/src/input.css -o static/css/output.css --watch
  ```
- Build de produção:
  ```
  tailwindcss -i static/src/input.css -o static/css/output.css --minify
  ```

O `output.css` é referenciado em `base.html` via `{% static %}`.
