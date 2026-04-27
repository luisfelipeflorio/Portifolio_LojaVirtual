# Data Models

## Model Base — TimeStampedModel

Todos os models do projeto herdam de `TimeStampedModel`, definido em `core/models.py`:

```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

---

## Schema ER

```
USER ||--o{ ADDRESS   : possui
USER ||--o{ ORDER     : realiza
CATEGORY ||--o{ PRODUCT  : contém
ORDER ||--o{ ORDER_ITEM  : possui
PRODUCT ||--o{ ORDER_ITEM : referenciado em
```

---

## Models

### accounts — CustomUser
Herda de `AbstractUser` + `TimeStampedModel`.

| Campo | Tipo | Observações |
|---|---|---|
| first_name | CharField | herdado |
| last_name | CharField | herdado |
| email | EmailField | herdado |
| password | — | hash via AbstractUser |
| phone | CharField(20) | `blank=True` |
| created_at / updated_at | DateTimeField | via TimeStampedModel |

`AUTH_USER_MODEL = 'accounts.CustomUser'` definido antes da primeira migration.

---

### accounts — Address

| Campo | Tipo | Observações |
|---|---|---|
| user | FK → CustomUser | `on_delete=CASCADE` |
| street | CharField | |
| number | CharField | |
| complement | CharField | `blank=True` |
| neighborhood | CharField | |
| city | CharField | |
| state | CharField | |
| zip_code | CharField | |
| is_default | BooleanField | `default=False` |

---

### catalog — Category

| Campo | Tipo | Observações |
|---|---|---|
| name | CharField | |
| slug | SlugField | auto-gerado via `save()` |
| description | TextField | |
| image | ImageField | |
| is_active | BooleanField | |
| sort_order | IntegerField | |

---

### catalog — Product

| Campo | Tipo | Observações |
|---|---|---|
| category | FK → Category | |
| name | CharField | |
| slug | SlugField | auto-gerado via `save()` |
| description | TextField | |
| price | DecimalField | |
| image | ImageField | |
| is_active | BooleanField | |
| is_featured | BooleanField | |
| is_promotion | BooleanField | |
| promotion_price | DecimalField | `null=True, blank=True` |
| stock | IntegerField | |

**Propriedade `current_price`:** retorna `promotion_price` se `is_promotion` else `price`.

---

### orders — Order

| Campo | Tipo | Observações |
|---|---|---|
| user | FK → CustomUser | `null=True` (compra sem login) |
| protocol | CharField | gerado em `save()` — ex: `CON-20260001` |
| status | CharField | choices: `received`, `preparing`, `ready`, `delivered` |
| delivery_type | CharField | choices: `pickup`, `delivery` |
| customer_name | CharField | |
| customer_email | EmailField | |
| customer_phone | CharField | |
| delivery_address | TextField | `blank=True` |
| scheduled_at | DateTimeField | data/hora desejada |
| notes | TextField | `blank=True` |
| subtotal | DecimalField | |
| delivery_fee | DecimalField | |
| total | DecimalField | |

---

### orders — OrderItem

| Campo | Tipo | Observações |
|---|---|---|
| order | FK → Order | `on_delete=CASCADE` |
| product | FK → Product | `null=True, on_delete=SET_NULL` |
| product_name | CharField | snapshot do nome no momento do pedido |
| unit_price | DecimalField | snapshot do preço |
| quantity | IntegerField | |
| subtotal | DecimalField | calculado em `save()`: `unit_price × quantity` |
