# Convenções de Código

## Padrões Gerais

- **PEP 8** em todo o código Python
- **Aspas simples** (`'`) em todo o projeto
- **Código em inglês** — variáveis, funções, classes, comentários
- **Interface em português brasileiro** — labels, mensagens, textos dos templates
- Sem over-engineering: a solução mais simples que resolve o problema

---

## Django

### Views

Preferência por **Class-Based Views (CBVs)**. Usar as genéricas do Django quando possível:

| Situação | CBV recomendada |
|---|---|
| Listar objetos | `ListView` |
| Detalhe de objeto | `DetailView` |
| Criar objeto | `CreateView` |
| Editar objeto | `UpdateView` |
| Deletar objeto | `DeleteView` |
| Renderizar template simples | `TemplateView` |
| Formulário customizado | `FormView` |
| Lógica customizada (POST puro) | `View` |

Autenticação nas views:
- Páginas de cliente logado: `LoginRequiredMixin`
- Páginas do dashboard admin: `StaffRequiredMixin` (definido em `dashboard/mixins.py`)

### Models

- Todo model herda de `TimeStampedModel` (campos `created_at` e `updated_at` automáticos)
- Slugs são auto-gerados via `slugify` no método `save()`
- `get_absolute_url()` implementado nos models que têm página pública

### Signals

- Signals ficam em `signals.py` dentro da app correspondente
- Conectados no método `ready()` do `AppConfig` em `apps.py`

```python
# orders/apps.py
class OrdersConfig(AppConfig):
    def ready(self):
        import orders.signals  # noqa
```

### Formulários

- Widgets estilizados com TailwindCSS via atributos `attrs` no `__init__` do formulário ou com `django-widget-tweaks` nos templates
- Mensagens de erro em português
- Validação customizada via método `clean()` / `clean_<campo>()`

### URL Namespaces

Cada app tem namespace definido em seu `urls.py`:

```python
app_name = 'catalog'
```

Referência nos templates: `{% url 'catalog:list' %}`, `{% url 'cart:detail' %}`, etc.

---

## Segurança

- CSRF protection nativo do Django habilitado em todos os formulários (`{% csrf_token %}`)
- Senhas com hash via `AbstractUser` — nunca armazenar em texto puro
- Dashboard restrito a `is_staff = True` via `StaffRequiredMixin`
- Variáveis sensíveis (`SECRET_KEY`, credenciais SMTP) exclusivamente no `.env`

---

## Templates

- Estendem `base.html` com `{% extends 'base.html' %}`
- Blocos mínimos: `{% block title %}` e `{% block content %}`
- Partials reutilizáveis com prefixo `_` (ex: `_product_card.html`, `_messages.html`)
- Sem frameworks JavaScript externos — JS vanilla quando necessário

---

## Carrinho

O carrinho é mantido na sessão Django (não exige login). A chave de sessão é gerenciada pela classe `Cart` em `cart/cart.py`. Após a finalização do pedido, `cart.clear()` é chamado.

Disponível em todos os templates via context processor `cart.context_processors.cart`, que injeta `cart_count`.
