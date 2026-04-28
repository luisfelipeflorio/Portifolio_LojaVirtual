## 13. Lista de Tarefas por Sprint

---

### Sprint 0 — Setup e Configuração do Projeto

#### Tarefa 0.1 — Estrutura inicial do projeto Django
- [X] 0.1.1 Criar o ambiente virtual Python com `python -m venv .venv`
- [X] 0.1.2 Instalar Django 5.x via pip e gerar `requirements.txt`
- [X] 0.1.3 Criar projeto Django com `django-admin startproject confeitaria .`
- [X] 0.1.4 Configurar `settings.py`: `LANGUAGE_CODE = 'pt-br'`, `TIME_ZONE = 'America/Sao_Paulo'`, `USE_I18N = True`
- [X] 0.1.5 Configurar `MEDIA_ROOT`, `MEDIA_URL` e servir arquivos de mídia no `urls.py` principal em modo `DEBUG`
- [X] 0.1.6 Configurar `STATIC_ROOT` e `STATICFILES_DIRS` para o TailwindCSS compilado
- [X] 0.1.7 Instalar `python-decouple` e criar arquivo `.env` com `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- [X] 0.1.8 Adicionar `.env` e `db.sqlite3` ao `.gitignore`
- [X] 0.1.9 Criar estrutura de pastas: `templates/`, `static/`, `media/`

#### Tarefa 0.2 — Instalação e configuração do TailwindCSS
- [X] 0.2.1 Baixar TailwindCSS CLI standalone (`.exe` ou binário) para a pasta do projeto
- [X] 0.2.2 Criar arquivo `tailwind.config.js` com `content` apontando para todos os templates Django (`templates/**/*.html`)
- [X] 0.2.3 Criar arquivo `static/src/input.css` com as diretivas `@tailwind base/components/utilities`
- [X] 0.2.4 Compilar o CSS com `tailwindcss -i static/src/input.css -o static/css/output.css --watch` em desenvolvimento
- [X] 0.2.5 Referenciar `static/css/output.css` no `base.html` via `{% static %}`

#### Tarefa 0.3 — Template base e layout global
- [X] 0.3.1 Criar `templates/base.html` com estrutura HTML5, meta tags responsivas, link para CSS compilado e Google Fonts
- [X] 0.3.2 Implementar navbar com gradiente rosa, logo, links de navegação e ícone de carrinho com contador
- [X] 0.3.3 Implementar footer simples com nome da confeitaria, redes sociais e horário de funcionamento
- [X] 0.3.4 Criar bloco `{% block content %}` e `{% block title %}` no `base.html`
- [X] 0.3.5 Criar template parcial `templates/_messages.html` para mensagens Django (`django.contrib.messages`)

#### Tarefa 0.4 — Criação das apps Django
- [X] 0.4.1 Criar app `core` com `python manage.py startapp core`
- [X] 0.4.2 Criar app `catalog` com `python manage.py startapp catalog`
- [X] 0.4.3 Criar app `cart` com `python manage.py startapp cart`
- [X] 0.4.4 Criar app `orders` com `python manage.py startapp orders`
- [X] 0.4.5 Criar app `accounts` com `python manage.py startapp accounts`
- [X] 0.4.6 Criar app `dashboard` com `python manage.py startapp dashboard`
- [X] 0.4.7 Registrar todas as apps em `INSTALLED_APPS` no `settings.py`
- [X] 0.4.8 Criar `urls.py` em cada app e incluir no `urls.py` principal com prefixos adequados

#### Tarefa 0.5 — Model base abstrato
- [X] 0.5.1 Criar arquivo `core/models.py` com model abstrato `TimeStampedModel` contendo `created_at = models.DateTimeField(auto_now_add=True)` e `updated_at = models.DateTimeField(auto_now=True)`
- [X] 0.5.2 Documentar no `TimeStampedModel` que todos os models do projeto devem herdar dele

---

### Sprint 1 — Autenticação e Perfil de Usuário

#### Tarefa 1.1 — Model de usuário customizado
- [X] 1.1.1 Criar model `CustomUser` em `accounts/models.py` herdando de `AbstractUser` e `TimeStampedModel`
- [X] 1.1.2 Adicionar campo `phone = models.CharField(max_length=20, blank=True)` ao `CustomUser`
- [X] 1.1.3 Definir `AUTH_USER_MODEL = 'accounts.CustomUser'` no `settings.py` **antes** da primeira migration
- [X] 1.1.4 Executar `python manage.py makemigrations accounts` e `python manage.py migrate`

#### Tarefa 1.2 — Model de endereço
- [X] 1.2.1 Criar model `Address` em `accounts/models.py` herdando de `TimeStampedModel`
- [X] 1.2.2 Campos: `user (FK)`, `street`, `number`, `complement (blank)`, `neighborhood`, `city`, `state`, `zip_code`, `is_default (bool, default=False)`
- [X] 1.2.3 Criar migration e migrar

#### Tarefa 1.3 — Formulários de autenticação
- [X] 1.3.1 Criar `accounts/forms.py` com `RegisterForm` herdando de `UserCreationForm` com campos: `first_name`, `last_name`, `email`, `phone`, `password1`, `password2`
- [X] 1.3.2 Criar `LoginForm` usando `AuthenticationForm` do Django
- [X] 1.3.3 Criar `ProfileForm` para edição de perfil com campos: `first_name`, `last_name`, `phone`
- [X] 1.3.4 Aplicar classes TailwindCSS nos widgets dos formulários via `django-widget-tweaks`

#### Tarefa 1.4 — Views de autenticação
- [X] 1.4.1 Criar `RegisterView` (CBV `CreateView`) em `accounts/views.py` que autentica o usuário automaticamente após cadastro
- [X] 1.4.2 Usar `LoginView` e `LogoutView` do `django.contrib.auth.views` configurados nas URLs
- [X] 1.4.3 Criar `ProfileView` (CBV `UpdateView` com `LoginRequiredMixin`) para edição de dados do usuário
- [X] 1.4.4 Configurar `LOGIN_REDIRECT_URL = 'core:home'` e `LOGOUT_REDIRECT_URL = 'core:home'` no `settings.py`

#### Tarefa 1.5 — Templates de autenticação
- [X] 1.5.1 Criar `templates/accounts/register.html` com formulário estilizado, link para login
- [X] 1.5.2 Criar `templates/accounts/login.html` com formulário estilizado, link para cadastro
- [X] 1.5.3 Criar `templates/accounts/profile.html` com formulário de edição e seção de histórico de pedidos (link)
- [X] 1.5.4 Atualizar navbar para exibir nome do usuário logado e link para perfil/logout, ou links de login/cadastro para visitantes

---

### Sprint 2 — Catálogo de Produtos [X]

#### Tarefa 2.1 — Models de Catálogo [X]
- [X] 2.1.1 Criar model `Category` em `catalog/models.py` herdando de `TimeStampedModel`; campos: `name`, `slug (auto)`, `description`, `image`, `is_active`, `sort_order`
- [X] 2.1.2 Criar model `Product` em `catalog/models.py` herdando de `TimeStampedModel`; campos: `category (FK)`, `name`, `slug (auto)`, `description`, `price`, `image`, `is_active`, `is_featured`, `is_promotion`, `promotion_price`, `stock`
- [X] 2.1.3 Sobrescrever método `save()` para auto-gerar `slug` a partir do `name` com `slugify`
- [X] 2.1.4 Adicionar `get_absolute_url()` ao model `Product` apontando para a view de detalhe
- [X] 2.1.5 Adicionar propriedade `current_price` ao `Product` que retorna `promotion_price` se `is_promotion` else `price`
- [X] 2.1.6 Registrar models no `catalog/admin.py` com `list_display`, `list_filter` e `search_fields` configurados
- [X] 2.1.7 Executar `makemigrations catalog` e `migrate`

#### Tarefa 2.2 — Views do catálogo [X]
- [X] 2.2.1 Criar `ProductListView` (CBV `ListView`) em `catalog/views.py` com queryset `Product.objects.filter(is_active=True)`
- [X] 2.2.2 Implementar filtragem por categoria via `get_queryset()` usando `self.request.GET.get('categoria')`
- [X] 2.2.3 Implementar busca por nome via `get_queryset()` usando `self.request.GET.get('q')`
- [X] 2.2.4 Passar lista de categorias ativas ao contexto via `get_context_data()` para o menu de filtros
- [X] 2.2.5 Criar `ProductDetailView` (CBV `DetailView`) com `queryset = Product.objects.filter(is_active=True)` e `slug_field = 'slug'`
- [X] 2.2.6 Configurar URLs em `catalog/urls.py`: `path('', ProductListView, name='list')` e `path('<slug:slug>/', ProductDetailView, name='detail')`

#### Tarefa 2.3 — Templates do catálogo [X]
- [X] 2.3.1 Criar `templates/catalog/product_list.html` estendendo `base.html`
- [X] 2.3.2 Implementar barra de filtros por categoria (pills/tabs com TailwindCSS) e campo de busca
- [X] 2.3.3 Implementar grid responsivo de cards de produto usando o padrão definido no Design System
- [X] 2.3.4 Criar partial `templates/catalog/_product_card.html` reutilizável com badge de promoção e destaque
- [X] 2.3.5 Criar `templates/catalog/product_detail.html` com imagem grande, nome, descrição, preço e botão "Adicionar ao carrinho"
- [X] 2.3.6 Implementar estado vazio (nenhum produto encontrado) com mensagem amigável

#### Tarefa 2.4 — Página inicial (core) [X]
- [X] 2.4.1 Criar `HomeView` (CBV `TemplateView`) em `core/views.py` que passa ao contexto: produtos em destaque (top 4) e categorias ativas
- [X] 2.4.2 Criar `templates/core/home.html` com seção hero (gradiente + chamada para ação), seção de destaques e seção de categorias
- [X] 2.4.3 Configurar URL `path('', HomeView, name='home')` em `core/urls.py` e incluir no `urls.py` principal

---

### Sprint 3 — Carrinho de Compras [X]

#### Tarefa 3.1 — Lógica do carrinho em sessão
- [X] 3.1.1 Criar `cart/cart.py` com classe `Cart` que gerencia o carrinho na sessão Django
- [X] 3.1.2 Implementar método `add(product, quantity=1)` que adiciona ou incrementa item na sessão
- [X] 3.1.3 Implementar método `remove(product_id)` que remove item da sessão
- [X] 3.1.4 Implementar método `update(product_id, quantity)` que atualiza a quantidade
- [X] 3.1.5 Implementar propriedade `total` que soma `price * quantity` de todos os itens
- [X] 3.1.6 Implementar método `__len__()` retornando a quantidade total de itens
- [X] 3.1.7 Implementar método `__iter__()` que itera sobre itens enriquecendo com objetos `Product` do banco
- [X] 3.1.8 Implementar método `clear()` para limpar o carrinho após pedido confirmado

#### Tarefa 3.2 — Context processor do carrinho
- [X] 3.2.1 Criar `cart/context_processors.py` com função `cart` que injeta `cart_count` em todos os templates
- [X] 3.2.2 Registrar o context processor em `settings.py` dentro de `TEMPLATES[0]['OPTIONS']['context_processors']`

#### Tarefa 3.3 — Views do carrinho
- [X] 3.3.1 Criar `CartDetailView` (CBV `View`) em `cart/views.py` que renderiza o carrinho atual
- [X] 3.3.2 Criar `CartAddView` (CBV `View`, método POST) que recebe `product_id` e `quantity` e adiciona ao carrinho, redirecionando com mensagem de sucesso
- [X] 3.3.3 Criar `CartRemoveView` (CBV `View`, método POST) que remove item do carrinho
- [X] 3.3.4 Criar `CartUpdateView` (CBV `View`, método POST) que atualiza quantidade de um item
- [X] 3.3.5 Configurar URLs em `cart/urls.py`

#### Tarefa 3.4 — Templates do carrinho
- [X] 3.4.1 Criar `templates/cart/detail.html` com tabela/lista de itens, colunas: produto, preço unitário, quantidade (inputs + / −), subtotal, ação remover
- [X] 3.4.2 Implementar totalizador: subtotal, frete (campo fixo "A combinar") e total
- [X] 3.4.3 Botão "Finalizar Pedido" levando ao checkout e botão "Continuar Comprando" voltando ao catálogo
- [X] 3.4.4 Exibir estado vazio do carrinho com mensagem e link para o catálogo

---

### Sprint 4 — Checkout e Pedidos [X]

#### Tarefa 4.1 — Models de pedido
- [X] 4.1.1 Criar model `Order` em `orders/models.py` herdando de `TimeStampedModel` com todos os campos definidos no schema ER
- [X] 4.1.2 Definir `STATUS_CHOICES` como tupla de constantes na própria model: `RECEIVED`, `PREPARING`, `READY`, `DELIVERED`
- [X] 4.1.3 Definir `DELIVERY_CHOICES`: `PICKUP` (retirada) e `DELIVERY` (entrega)
- [X] 4.1.4 Implementar método `generate_protocol()` que gera protocolo único (ex: `CON-{ano}{random 4 digitos}`) e chamá-lo no `save()` quando `protocol` estiver vazio
- [X] 4.1.5 Criar model `OrderItem` em `orders/models.py` herdando de `TimeStampedModel` com campos: `order (FK)`, `product (FK null=True on_delete=SET_NULL)`, `product_name`, `unit_price`, `quantity`, `subtotal`
- [X] 4.1.6 Implementar método `save()` no `OrderItem` para calcular `subtotal = unit_price * quantity` automaticamente
- [X] 4.1.7 Registrar models no `orders/admin.py` com inline de `OrderItem` dentro de `Order`
- [X] 4.1.8 Executar `makemigrations orders` e `migrate`

#### Tarefa 4.2 — Formulário de checkout
- [ ] 4.2.1 Criar `orders/forms.py` com `CheckoutForm` baseado em `forms.Form` (não ModelForm) com campos: `customer_name`, `customer_email`, `customer_phone`, `delivery_type` (RadioSelect), `delivery_address` (Textarea, required=False), `scheduled_at` (DateTimeInput), `notes` (Textarea, required=False)
- [ ] 4.2.2 Implementar validação `clean()` que exige `delivery_address` se `delivery_type == 'delivery'`
- [ ] 4.2.3 Aplicar classes TailwindCSS nos widgets via atributos `attrs` no `__init__` do formulário

#### Tarefa 4.3 — Views de checkout e pedido
- [X] 4.3.1 Criar `CheckoutView` (CBV `FormView`) em `orders/views.py` que renderiza o formulário de checkout
- [X] 4.3.2 No método `get_initial()`, pré-preencher dados do cliente logado se `request.user.is_authenticated`
- [X] 4.3.3 No método `form_valid()`: criar `Order`, criar `OrderItem` para cada item do carrinho, chamar `cart.clear()`, disparar e-mail de confirmação e redirecionar para página de sucesso
- [X] 4.3.4 Criar `OrderSuccessView` (CBV `DetailView`) que exibe página de confirmação com protocolo, buscando a `Order` pelo `pk` ou `protocol`
- [X] 4.3.5 Criar `OrderHistoryView` (CBV `ListView` com `LoginRequiredMixin`) que lista pedidos do usuário logado ordenados por `-created_at`
- [X] 4.3.6 Criar `OrderDetailView` (CBV `DetailView` com `LoginRequiredMixin`) que exibe detalhe de um pedido do usuário logado (verificar `order.user == request.user`)
- [X] 4.3.7 Configurar URLs em `orders/urls.py`

#### Tarefa 4.4 — Templates de checkout e pedido
- [X] 4.4.1 Criar `templates/orders/checkout.html` com formulário em duas colunas (dados do cliente | resumo do pedido)
- [X] 4.4.2 Implementar toggle JS vanilla para mostrar/ocultar campo de endereço conforme seleção de `delivery_type`
- [X] 4.4.3 Criar `templates/orders/order_success.html` com card de confirmação: protocolo em destaque, lista de itens, total, mensagem de agradecimento e link para home
- [X] 4.4.4 Criar `templates/orders/order_history.html` com tabela de pedidos: protocolo, data, total, status (badge colorido), link "Ver detalhe"
- [X] 4.4.5 Criar `templates/orders/order_detail.html` com detalhe completo do pedido: dados do cliente, itens, endereço de entrega, observações e status atual

#### Tarefa 4.5 — E-mail de confirmação de pedido
- [X] 4.5.1 Criar `orders/signals.py` com signal `post_save` no model `Order` que dispara e-mail de confirmação ao cliente quando `created=True`
- [X] 4.5.2 Conectar signal no `orders/apps.py` via método `ready()`
- [X] 4.5.3 Criar template de e-mail `templates/orders/email/order_confirmation.html` com dados do pedido formatados
- [X] 4.5.4 Criar template de e-mail texto puro `templates/orders/email/order_confirmation.txt`
- [X] 4.5.5 Configurar `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` em desenvolvimento no `settings.py`

---

### Sprint 5 — Painel Administrativo

#### Tarefa 5.1 — Dashboard principal
- [ ] 5.1.1 Criar `DashboardHomeView` (CBV `TemplateView` com `LoginRequiredMixin`) em `dashboard/views.py` com verificação `if not request.user.is_staff: raise PermissionDenied`
- [ ] 5.1.2 Calcular no `get_context_data()`: total de pedidos hoje, receita do dia, pedidos pendentes (status `received` ou `preparing`), pedidos prontos (status `ready`)
- [ ] 5.1.3 Criar `templates/dashboard/home.html` com grid de cards de KPI (4 cards no topo) e lista dos 10 pedidos mais recentes
- [ ] 5.1.4 Criar layout base do dashboard `templates/dashboard/base_dashboard.html` com sidebar de navegação e conteúdo principal

#### Tarefa 5.2 — Gestão de categorias
- [ ] 5.2.1 Criar `CategoryListView` (CBV `ListView`) em `dashboard/views.py`
- [ ] 5.2.2 Criar `CategoryCreateView` (CBV `CreateView`) com `fields = ['name', 'description', 'image', 'is_active', 'sort_order']`
- [ ] 5.2.3 Criar `CategoryUpdateView` (CBV `UpdateView`) com os mesmos campos
- [ ] 5.2.4 Criar `CategoryDeleteView` (CBV `DeleteView`) com confirmação
- [ ] 5.2.5 Criar templates: `dashboard/category_list.html`, `dashboard/category_form.html`, `dashboard/category_confirm_delete.html`

#### Tarefa 5.3 — Gestão de produtos
- [ ] 5.3.1 Criar `ProductListView` (CBV `ListView`) em `dashboard/views.py` com filtro por categoria e status
- [ ] 5.3.2 Criar `ProductCreateView` (CBV `CreateView`) com todos os campos do model `Product`
- [ ] 5.3.3 Criar `ProductUpdateView` (CBV `UpdateView`) com os mesmos campos
- [ ] 5.3.4 Criar `ProductDeleteView` (CBV `DeleteView`) com confirmação
- [ ] 5.3.5 Criar templates: `dashboard/product_list.html` (tabela com imagem miniatura, preço, status), `dashboard/product_form.html`, `dashboard/product_confirm_delete.html`
- [ ] 5.3.6 Implementar preview de imagem no formulário de produto via JS vanilla

#### Tarefa 5.4 — Gestão de pedidos
- [ ] 5.4.1 Criar `OrderListView` (CBV `ListView`) em `dashboard/views.py` com filtros por status e data via GET params
- [ ] 5.4.2 Criar `OrderDetailAdminView` (CBV `DetailView`) que exibe todos os dados do pedido para o admin
- [ ] 5.4.3 Criar `OrderStatusUpdateView` (CBV `View`, método POST) que recebe `order_id` e `status` e atualiza o model
- [ ] 5.4.4 No `OrderStatusUpdateView`, após salvar, disparar signal ou chamar função que envia e-mail de atualização ao cliente
- [ ] 5.4.5 Criar `orders/signals.py` com signal `post_save` que detecta mudança de `status` e envia e-mail de atualização (verificar se `status` realmente mudou comparando com versão anterior)
- [ ] 5.4.6 Criar templates: `dashboard/order_list.html` (tabela com filtros e badges de status), `dashboard/order_detail.html`, `dashboard/order_status_form.html` (dropdown de status + botão salvar)

#### Tarefa 5.5 — Mixin de segurança para o dashboard
- [ ] 5.5.1 Criar `dashboard/mixins.py` com `StaffRequiredMixin` herdando de `LoginRequiredMixin` que verifica `request.user.is_staff` e lança `PermissionDenied` caso contrário
- [ ] 5.5.2 Aplicar `StaffRequiredMixin` em todas as views do dashboard (substituindo implementações inline)

---

### Sprint 6 — Polimento, SEO e Ajustes Finais

#### Tarefa 6.1 — Polimento de UI
- [ ] 6.1.1 Revisar responsividade de todos os templates em mobile (375px), tablet (768px) e desktop (1280px)
- [ ] 6.1.2 Adicionar estados de loading/disabled nos botões de formulário para prevenir duplo envio
- [ ] 6.1.3 Implementar mensagens de feedback (django.contrib.messages) em todas as ações com estilo TailwindCSS
- [ ] 6.1.4 Revisar contraste de texto conforme WCAG AA em todos os componentes

#### Tarefa 6.2 — SEO básico
- [ ] 6.2.1 Adicionar `<meta name="description">` em `base.html` com bloco sobrescrevível por cada template
- [ ] 6.2.2 Adicionar `<title>{% block title %}{% endblock %} | Confeitaria</title>` dinâmico
- [ ] 6.2.3 Adicionar `alt` descritivo em todas as tags `<img>` dos templates
- [ ] 6.2.4 Criar `sitemap.xml` básico usando `django.contrib.sitemaps`

#### Tarefa 6.3 — Configurações de produção
- [ ] 6.3.1 Separar `settings.py` em `settings/base.py`, `settings/development.py` e `settings/production.py`
- [ ] 6.3.2 Configurar `ALLOWED_HOSTS` e `DEBUG=False` via `.env` para produção
- [ ] 6.3.3 Configurar servidor de e-mail SMTP real nas variáveis de ambiente de produção
- [ ] 6.3.4 Adicionar `WhiteNoise` para servir arquivos estáticos em produção
- [ ] 6.3.5 Executar `python manage.py collectstatic` e verificar que todos os arquivos estáticos são coletados corretamente

#### Tarefa 6.4 — Build final do TailwindCSS
- [ ] 6.4.1 Executar build de produção do TailwindCSS com `--minify`: `tailwindcss -i static/src/input.css -o static/css/output.css --minify`
- [ ] 6.4.2 Verificar que todos os utilitários usados nos templates são gerados corretamente (sem classes purgadas indevidamente)
- [ ] 6.4.3 Documentar o comando de build no `README.md`

---

### Sprint 7 — Testes (Sprint Final)

#### Tarefa 7.1 — Testes unitários dos models
- [ ] 7.1.1 Escrever testes para `TimeStampedModel`: verificar que `created_at` e `updated_at` são preenchidos automaticamente
- [ ] 7.1.2 Escrever testes para `Product.current_price`: retorna `promotion_price` quando `is_promotion=True`
- [ ] 7.1.3 Escrever testes para `Order.generate_protocol()`: protocolo é único e gerado no save
- [ ] 7.1.4 Escrever testes para `OrderItem.save()`: `subtotal` calculado corretamente

#### Tarefa 7.2 — Testes de views e fluxos
- [ ] 7.2.1 Escrever testes para o fluxo completo de carrinho (add, update, remove, total)
- [ ] 7.2.2 Escrever testes para o fluxo de checkout: formulário válido cria `Order` e `OrderItem`s
- [ ] 7.2.3 Escrever testes para `StaffRequiredMixin`: usuário não-staff recebe 403
- [ ] 7.2.4 Escrever testes para atualização de status de pedido no dashboard

---

### Sprint 8 — Docker e Deploy (Sprint Final)

#### Tarefa 8.1 — Containerização
- [ ] 8.1.1 Criar `Dockerfile` para a aplicação Django com Python 3.12 slim
- [ ] 8.1.2 Criar `docker-compose.yml` com serviço `web` (Django + Gunicorn) e serviço `nginx` (proxy reverso)
- [ ] 8.1.3 Configurar volume para `MEDIA_ROOT` persistente no Docker
- [ ] 8.1.4 Criar script `entrypoint.sh` que executa `migrate`, `collectstatic` e inicia o Gunicorn
- [ ] 8.1.5 Testar o build completo com `docker-compose up --build` e validar todos os fluxos

#### Tarefa 8.2 — Deploy
- [ ] 8.2.1 Configurar servidor (VPS ou PaaS como Railway/Render)
- [ ] 8.2.2 Configurar variáveis de ambiente de produção no servidor
- [ ] 8.2.3 Configurar HTTPS com certificado SSL
- [ ] 8.2.4 Realizar deploy e smoke test de todos os fluxos principais em produção
