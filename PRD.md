# PRD — Loja Virtual de Confeitaria

---

## 1. Visão Geral

Este documento descreve os requisitos de produto para uma loja virtual de confeitaria artesanal, desenvolvida com Python/Django full stack e TailwindCSS. O sistema permite que clientes naveguem pelo cardápio, montem pedidos personalizados e realizem a compra de produtos como bolos, doces e salgados, com gestão completa pelo painel administrativo da confeitaria.

---

## 2. Sobre o Produto

**Nome provisório:** Confeitaria Virtual  
**Tipo:** E-commerce B2C especializado em confeitaria artesanal  
**Plataforma:** Web responsiva (desktop, tablet e mobile)  
**Stack principal:** Python 3.12 · Django 5.x · SQLite · TailwindCSS 3.x  
**Modo de entrega:** Retirada no local e entrega por delivery (área de cobertura configurável)

O produto é uma loja virtual simples e funcional, sem over engineering, que centraliza o catálogo de produtos, o fluxo de pedidos e a comunicação com o cliente em um único sistema Django full stack.

---

## 3. Propósito

Digitalizar o processo de vendas de uma confeitaria artesanal, eliminando pedidos por WhatsApp/telefone com agendas manuais, reduzindo erros operacionais e oferecendo ao cliente uma experiência de compra clara, bonita e intuitiva, mesmo em dispositivos móveis.

---

## 4. Público-Alvo

| Perfil | Descrição |
|---|---|
| **Cliente final** | Adultos de 25–55 anos, região local/delivery, com acesso a smartphone ou computador, que buscam bolos e doces para ocasiões especiais ou consumo rotineiro |
| **Administrador** | Proprietário ou funcionário da confeitaria, com baixo conhecimento técnico, que precisa gerenciar catálogo, pedidos e status sem depender de desenvolvedores |

---

## 5. Objetivos

### 5.1 Objetivos de Negócio
- Aumentar o volume de pedidos ao facilitar o processo de compra online
- Reduzir o tempo gasto com atendimento manual via WhatsApp
- Centralizar o controle de pedidos em um único painel

### 5.2 Objetivos de Produto
- Entregar um catálogo de produtos navegável e filtrável por categoria
- Implementar fluxo de carrinho → checkout → confirmação de pedido
- Disponibilizar painel administrativo para gestão de produtos e pedidos
- Garantir design responsivo e moderno com identidade visual de confeitaria

### 5.3 Objetivos Técnicos
- Código simples, legível e aderente à PEP 8
- Django full stack sem frameworks JS externos
- Zero dependência de Docker na fase inicial
- Banco de dados SQLite nativo do Django

---

## 6. Requisitos Funcionais

### 6.1 Módulo de Catálogo
- RF01 — Listar produtos por categoria (bolos, doces, salgados, bebidas)
- RF02 — Exibir página de detalhe do produto com foto, descrição, preço e opções de personalização
- RF03 — Filtrar produtos por categoria e busca por nome
- RF04 — Destacar produtos em promoção e mais vendidos

### 6.2 Módulo de Carrinho
- RF05 — Adicionar/remover produtos ao carrinho (sessão Django)
- RF06 — Alterar quantidade de itens no carrinho
- RF07 — Exibir subtotal, frete estimado e total
- RF08 — Persistir carrinho na sessão sem exigir login

### 6.3 Módulo de Checkout
- RF09 — Formulário de dados do cliente (nome, telefone, e-mail)
- RF10 — Seleção de modo de entrega: retirada ou delivery
- RF11 — Campo de endereço condicional (apenas para delivery)
- RF12 — Campo de observações/personalizações do pedido
- RF13 — Seleção de data/hora desejada para retirada ou entrega
- RF14 — Resumo do pedido antes da confirmação
- RF15 — Confirmação de pedido com número de protocolo

### 6.4 Módulo de Autenticação
- RF16 — Cadastro e login de clientes (e-mail + senha)
- RF17 — Histórico de pedidos para clientes logados
- RF18 — Edição de perfil e endereços salvos

### 6.5 Módulo Administrativo
- RF19 — CRUD de categorias de produtos
- RF20 — CRUD de produtos (nome, descrição, foto, preço, estoque, destaque, ativo)
- RF21 — Listagem de pedidos com filtro por status e data
- RF22 — Atualização de status do pedido (Recebido → Em preparo → Pronto → Entregue)
- RF23 — Visualização do detalhe de cada pedido
- RF24 — Dashboard com resumo do dia (total de pedidos, receita, pedidos pendentes)

### 6.6 Módulo de Notificações
- RF25 — E-mail de confirmação de pedido ao cliente
- RF26 — E-mail de atualização de status ao cliente

---

### 6.7 Fluxos de UX — Flowcharts

#### Fluxo do Cliente — Compra

```mermaid
flowchart TD
    A([Acessa a loja]) --> B[Página Inicial]
    B --> C{Navega pelo catálogo}
    C --> D[Lista de produtos por categoria]
    C --> E[Busca por nome]
    D --> F[Detalhe do produto]
    E --> F
    F --> G[Adiciona ao carrinho]
    G --> H{Continua comprando?}
    H -- Sim --> C
    H -- Não --> I[Visualiza carrinho]
    I --> J{Ajusta quantidades?}
    J -- Sim --> I
    J -- Não --> K[Inicia checkout]
    K --> L{Está logado?}
    L -- Não --> M[Preenche dados como visitante]
    L -- Sim --> N[Dados pré-preenchidos do perfil]
    M --> O[Seleciona modo de entrega]
    N --> O
    O --> P{Delivery?}
    P -- Sim --> Q[Preenche endereço]
    P -- Não --> R[Define data/hora de retirada]
    Q --> S[Preenche observações]
    R --> S
    S --> T[Revisa resumo do pedido]
    T --> U[Confirma pedido]
    U --> V[Página de confirmação com protocolo]
    V --> W[Recebe e-mail de confirmação]
```

#### Fluxo do Administrador — Gestão de Pedidos

```mermaid
flowchart TD
    A([Admin acessa painel]) --> B[Dashboard]
    B --> C[Lista de pedidos do dia]
    C --> D[Visualiza detalhe do pedido]
    D --> E{Atualiza status}
    E --> F[Recebido]
    E --> G[Em preparo]
    E --> H[Pronto]
    E --> I[Entregue / Retirado]
    F --> J[Cliente recebe e-mail de atualização]
    G --> J
    H --> J
    I --> J
```

#### Fluxo de Autenticação

```mermaid
flowchart TD
    A([Usuário acessa a loja]) --> B{Tem conta?}
    B -- Não --> C[Página de cadastro]
    C --> D[Preenche nome, e-mail, senha]
    D --> E[Conta criada]
    E --> F[Redireciona para página inicial logado]
    B -- Sim --> G[Página de login]
    G --> H[Insere e-mail e senha]
    H --> I{Credenciais válidas?}
    I -- Sim --> F
    I -- Não --> J[Exibe erro]
    J --> G
```

---

## 7. Requisitos Não-Funcionais

| ID | Categoria | Requisito |
|---|---|---|
| RNF01 | Código | Aderência à PEP 8; aspas simples; código em inglês |
| RNF02 | Código | Class Based Views preferencialmente; sem over engineering |
| RNF03 | Banco de dados | SQLite nativo do Django; todo model com `created_at` e `updated_at` |
| RNF04 | Frontend | Django Template Language + TailwindCSS; sem frameworks JS externos |
| RNF05 | UI | Design responsivo (mobile-first); gradientes harmônicos |
| RNF06 | UI | Toda interface em português brasileiro |
| RNF07 | Segurança | CSRF protection nativo do Django; senhas com hash via `AbstractUser` |
| RNF08 | Signals | Signals em arquivo `signals.py` dentro da app correspondente |
| RNF09 | Infra | Sem Docker na fase inicial |
| RNF10 | Testes | Sem testes na fase inicial (sprints finais) |
| RNF11 | Performance | Páginas carregando em menos de 2s em conexão 4G |
| RNF12 | Manutenção | Admin padrão do Django extendido para gestão operacional |

---

## 8. Arquitetura Técnica

### 8.1 Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12 |
| Framework web | Django 5.x |
| Banco de dados | SQLite (django.db.backends.sqlite3) |
| Frontend | Django Template Language + TailwindCSS 3.x (via CLI standalone) |
| E-mail | Django `send_mail` com SMTP configurável (Gmail/Mailtrap) |
| Armazenamento de mídia | Django `FileField` / `ImageField` com `MEDIA_ROOT` local |
| Ambiente | `python-decouple` para variáveis de ambiente via `.env` |
| Dependências | `Pillow` (imagens), `django-widget-tweaks` (formulários) |

### 8.2 Estrutura de Apps Django

```
confeitaria/           ← projeto Django (settings, urls, wsgi)
├── core/              ← app base: home, páginas estáticas, contexto global
├── catalog/           ← categorias e produtos
├── cart/              ← carrinho via sessão
├── orders/            ← pedidos, itens de pedido, status
├── accounts/          ← cadastro, login, perfil, endereços
└── dashboard/         ← painel administrativo customizado
```

### 8.3 Estrutura de Dados — Schema ER

```mermaid
erDiagram
    USER {
        int id PK
        string first_name
        string last_name
        string email
        string password
        string phone
        datetime created_at
        datetime updated_at
    }

    ADDRESS {
        int id PK
        int user_id FK
        string street
        string number
        string complement
        string neighborhood
        string city
        string state
        string zip_code
        bool is_default
        datetime created_at
        datetime updated_at
    }

    CATEGORY {
        int id PK
        string name
        string slug
        string description
        string image
        bool is_active
        int sort_order
        datetime created_at
        datetime updated_at
    }

    PRODUCT {
        int id PK
        int category_id FK
        string name
        string slug
        string description
        decimal price
        string image
        bool is_active
        bool is_featured
        bool is_promotion
        decimal promotion_price
        int stock
        datetime created_at
        datetime updated_at
    }

    ORDER {
        int id PK
        int user_id FK
        string protocol
        string status
        string delivery_type
        string customer_name
        string customer_email
        string customer_phone
        text delivery_address
        datetime scheduled_at
        text notes
        decimal subtotal
        decimal delivery_fee
        decimal total
        datetime created_at
        datetime updated_at
    }

    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        string product_name
        decimal unit_price
        int quantity
        decimal subtotal
        datetime created_at
        datetime updated_at
    }

    USER ||--o{ ADDRESS : "possui"
    USER ||--o{ ORDER : "realiza"
    CATEGORY ||--o{ PRODUCT : "contém"
    ORDER ||--o{ ORDER_ITEM : "possui"
    PRODUCT ||--o{ ORDER_ITEM : "referenciado em"
```

---

## 9. Design System

### 9.1 Paleta de Cores

Paleta inspirada em confeitaria artesanal: tons rosados, cremes aquecidos, chocolates e dourados.

| Token | Nome | Hex | Uso |
|---|---|---|---|
| `primary-50` | Rosa Pétala | `#FFF1F3` | Fundos suaves |
| `primary-100` | Rosa Creme | `#FFE4E8` | Cards, hover suave |
| `primary-400` | Rosa Vibrante | `#FB7185` | Destaques, badges |
| `primary-500` | Rosa Principal | `#F43F5E` | Botão primário, links ativos |
| `primary-600` | Rosa Escuro | `#E11D48` | Hover botão primário |
| `secondary-400` | Caramelo Claro | `#FBBF24` | Badges promoção, ícones |
| `secondary-500` | Dourado | `#F59E0B` | Destaque premium |
| `brown-600` | Chocolate | `#92400E` | Texto secundário, bordas |
| `brown-800` | Cacau | `#451A03` | Texto em fundos claros |
| `neutral-50` | Creme Off-White | `#FAFAF9` | Background geral |
| `neutral-100` | Creme Suave | `#F5F5F4` | Background de seções |
| `neutral-600` | Cinza Médio | `#57534E` | Texto corpo |
| `neutral-900` | Quase Preto | `#1C1917` | Títulos |

### 9.2 Gradientes

```html
<!-- Gradiente hero principal -->
<div class="bg-gradient-to-br from-rose-50 via-pink-100 to-rose-200">

<!-- Gradiente botão primário -->
<button class="bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-600 hover:to-pink-700">

<!-- Gradiente card destaque -->
<div class="bg-gradient-to-br from-amber-50 to-rose-50">

<!-- Gradiente header/navbar -->
<nav class="bg-gradient-to-r from-rose-700 via-pink-600 to-rose-500">
```

### 9.3 Tipografia

```html
<!-- Fonte: Google Fonts via link no base.html -->
<!-- Títulos: Playfair Display (serif elegante) -->
<!-- Corpo: Inter (sans-serif legível) -->

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

```html
<!-- Título de página -->
<h1 class="font-['Playfair_Display'] text-3xl md:text-4xl font-bold text-neutral-900">

<!-- Título de seção -->
<h2 class="font-['Playfair_Display'] text-2xl font-semibold text-neutral-800">

<!-- Texto corpo -->
<p class="font-['Inter'] text-base text-neutral-600 leading-relaxed">

<!-- Label e caption -->
<span class="font-['Inter'] text-sm font-medium text-neutral-500">
```

### 9.4 Botões

```html
<!-- Botão Primário -->
<button class="bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-600 hover:to-pink-700
               text-white font-medium px-6 py-3 rounded-xl shadow-md
               hover:shadow-lg transition-all duration-200 cursor-pointer">
  Adicionar ao Carrinho
</button>

<!-- Botão Secundário (outline) -->
<button class="border-2 border-rose-500 text-rose-600 hover:bg-rose-50
               font-medium px-6 py-3 rounded-xl transition-all duration-200 cursor-pointer">
  Ver Detalhes
</button>

<!-- Botão Ghost -->
<button class="text-rose-600 hover:text-rose-700 hover:bg-rose-50
               font-medium px-4 py-2 rounded-lg transition-all duration-200 cursor-pointer">
  Cancelar
</button>

<!-- Botão Perigo -->
<button class="bg-red-500 hover:bg-red-600 text-white
               font-medium px-4 py-2 rounded-lg transition-all duration-200 cursor-pointer">
  Remover
</button>

<!-- Botão Admin / Ação administrativa -->
<button class="bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-500 hover:to-amber-600
               text-white font-medium px-5 py-2.5 rounded-lg shadow-sm
               transition-all duration-200 cursor-pointer">
  Salvar Produto
</button>
```

### 9.5 Inputs e Formulários

```html
<!-- Input padrão -->
<div class="flex flex-col gap-1">
  <label class="text-sm font-medium text-neutral-700">Nome completo</label>
  <input type="text"
         class="w-full px-4 py-3 rounded-xl border border-neutral-200
                bg-white focus:outline-none focus:ring-2 focus:ring-rose-400
                focus:border-transparent placeholder-neutral-400
                text-neutral-800 transition-all duration-200"
         placeholder="Digite seu nome">
</div>

<!-- Input com erro (django-widget-tweaks ou classe condicional) -->
<input type="text"
       class="w-full px-4 py-3 rounded-xl border border-red-400
              bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-400
              text-neutral-800 transition-all duration-200">
<span class="text-xs text-red-500 mt-1">Este campo é obrigatório.</span>

<!-- Select -->
<select class="w-full px-4 py-3 rounded-xl border border-neutral-200
               bg-white focus:outline-none focus:ring-2 focus:ring-rose-400
               text-neutral-800 cursor-pointer transition-all duration-200">
  <option>Selecione uma categoria</option>
</select>

<!-- Textarea -->
<textarea rows="4"
          class="w-full px-4 py-3 rounded-xl border border-neutral-200
                 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400
                 text-neutral-800 resize-none transition-all duration-200">
</textarea>
```

### 9.6 Cards de Produto

```html
<!-- Card de produto -->
<div class="bg-white rounded-2xl shadow-sm hover:shadow-md border border-neutral-100
            overflow-hidden transition-all duration-200 group">
  <div class="relative overflow-hidden">
    <img src="..." alt="..."
         class="w-full h-52 object-cover group-hover:scale-105 transition-transform duration-300">
    {% if product.is_promotion %}
    <span class="absolute top-3 left-3 bg-amber-400 text-white text-xs font-semibold px-2 py-1 rounded-full">
      Promoção
    </span>
    {% endif %}
    {% if product.is_featured %}
    <span class="absolute top-3 right-3 bg-rose-500 text-white text-xs font-semibold px-2 py-1 rounded-full">
      Destaque
    </span>
    {% endif %}
  </div>
  <div class="p-4">
    <h3 class="font-['Playfair_Display'] font-semibold text-neutral-900 text-lg">{{ product.name }}</h3>
    <p class="text-sm text-neutral-500 mt-1 line-clamp-2">{{ product.description }}</p>
    <div class="flex items-center justify-between mt-4">
      <span class="text-rose-600 font-bold text-xl">R$ {{ product.price }}</span>
      <button class="bg-gradient-to-r from-rose-500 to-pink-600 text-white
                     text-sm font-medium px-4 py-2 rounded-xl hover:shadow-md
                     transition-all duration-200 cursor-pointer">
        Adicionar
      </button>
    </div>
  </div>
</div>
```

### 9.7 Navbar

```html
<nav class="bg-gradient-to-r from-rose-700 via-pink-600 to-rose-500 shadow-lg sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <!-- Logo -->
      <a href="{% url 'core:home' %}" class="font-['Playfair_Display'] text-white text-2xl font-bold">
        🎂 Confeitaria
      </a>
      <!-- Links desktop -->
      <div class="hidden md:flex items-center gap-6">
        <a href="{% url 'catalog:list' %}" class="text-rose-100 hover:text-white font-medium transition-colors">
          Cardápio
        </a>
        <!-- Carrinho -->
        <a href="{% url 'cart:detail' %}" class="relative text-white">
          <span class="text-xl">🛒</span>
          <span class="absolute -top-2 -right-2 bg-amber-400 text-white text-xs rounded-full w-5 h-5
                       flex items-center justify-center font-bold">
            {{ cart_count }}
          </span>
        </a>
      </div>
    </div>
  </div>
</nav>
```

### 9.8 Grid de Produtos

```html
<!-- Grid responsivo de produtos -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  {% for product in products %}
    {% include 'catalog/_product_card.html' %}
  {% endfor %}
</div>
```

### 9.9 Badges de Status de Pedido

```html
<!-- Status badges -->
{% if order.status == 'received' %}
  <span class="bg-blue-100 text-blue-700 text-xs font-semibold px-3 py-1 rounded-full">Recebido</span>
{% elif order.status == 'preparing' %}
  <span class="bg-amber-100 text-amber-700 text-xs font-semibold px-3 py-1 rounded-full">Em preparo</span>
{% elif order.status == 'ready' %}
  <span class="bg-green-100 text-green-700 text-xs font-semibold px-3 py-1 rounded-full">Pronto</span>
{% elif order.status == 'delivered' %}
  <span class="bg-neutral-100 text-neutral-600 text-xs font-semibold px-3 py-1 rounded-full">Entregue</span>
{% endif %}
```

---

## 10. User Stories

### Épico 1 — Catálogo de Produtos

| ID | Como... | Quero... | Para... |
|---|---|---|---|
| US01 | Cliente | Ver todos os produtos organizados por categoria | Encontrar facilmente o que desejo |
| US02 | Cliente | Visualizar foto, descrição e preço detalhados de um produto | Tomar decisão de compra informada |
| US03 | Cliente | Filtrar produtos por categoria e buscar por nome | Agilizar minha navegação |
| US04 | Cliente | Ver produtos em destaque e promoções na página inicial | Não perder ofertas especiais |

**Critérios de aceite — US01:**
- [ ] Página de catálogo exibe todos os produtos ativos
- [ ] Filtro por categoria funciona via GET param `?categoria=slug`
- [ ] Busca por nome funciona via GET param `?q=termo`
- [ ] Produtos inativos não aparecem para o cliente
- [ ] Grid é responsivo (1 col mobile, 2 tablet, 3-4 desktop)

**Critérios de aceite — US02:**
- [ ] Página de detalhe exibe imagem, nome, descrição completa e preço
- [ ] Se produto em promoção, exibe preço original riscado e preço promocional
- [ ] Botão "Adicionar ao carrinho" presente e funcional
- [ ] Exibe categoria do produto com link de volta ao catálogo

---

### Épico 2 — Carrinho de Compras

| ID | Como... | Quero... | Para... |
|---|---|---|---|
| US05 | Cliente | Adicionar produtos ao carrinho sem precisar fazer login | Comprar de forma ágil |
| US06 | Cliente | Ajustar quantidades e remover itens do carrinho | Revisar meu pedido antes de confirmar |
| US07 | Cliente | Ver o resumo do carrinho com subtotal e total | Saber quanto estou gastando |

**Critérios de aceite — US05:**
- [ ] Carrinho persiste na sessão Django sem necessidade de login
- [ ] Adicionar o mesmo produto incrementa a quantidade
- [ ] Ícone na navbar exibe contagem de itens no carrinho
- [ ] Feedback visual (mensagem) ao adicionar item

**Critérios de aceite — US06:**
- [ ] Botões + e − ajustam quantidade; ao chegar em 0, item é removido
- [ ] Botão "Remover" exclui o item diretamente
- [ ] Total é recalculado em tempo real após cada alteração

---

### Épico 3 — Checkout e Pedido

| ID | Como... | Quero... | Para... |
|---|---|---|---|
| US08 | Cliente | Finalizar a compra informando meus dados | Receber meu pedido corretamente |
| US09 | Cliente | Escolher entre retirada e delivery | Adequar à minha necessidade |
| US10 | Cliente | Adicionar observações ao pedido | Personalizar meu bolo ou produto |
| US11 | Cliente | Receber confirmação por e-mail | Ter comprovante do pedido |

**Critérios de aceite — US08:**
- [ ] Formulário de checkout com nome, e-mail e telefone obrigatórios
- [ ] Validação de campos com mensagens de erro em português
- [ ] Se logado, dados do perfil são pré-preenchidos

**Critérios de aceite — US09:**
- [ ] Campo de endereço aparece apenas quando "Delivery" é selecionado
- [ ] Campo de data/hora agendada é obrigatório em ambos os modos
- [ ] Frete é exibido (pode ser valor fixo ou "a combinar")

**Critérios de aceite — US11:**
- [ ] E-mail enviado com protocolo, itens, total e observações
- [ ] Página de confirmação exibe número de protocolo único
- [ ] Protocolo é gerado automaticamente (UUID curto ou sequencial)

---

### Épico 4 — Autenticação e Perfil

| ID | Como... | Quero... | Para... |
|---|---|---|---|
| US12 | Cliente | Me cadastrar com e-mail e senha | Ter acesso ao histórico de pedidos |
| US13 | Cliente | Fazer login e logout | Acessar minha conta com segurança |
| US14 | Cliente | Ver meu histórico de pedidos | Acompanhar pedidos passados |
| US15 | Cliente | Editar meus dados e endereços | Manter informações atualizadas |

**Critérios de aceite — US12:**
- [ ] Formulário de cadastro valida e-mail único e senha com confirmação
- [ ] Após cadastro, usuário é logado automaticamente e redirecionado para home
- [ ] Senhas armazenadas com hash via Django AbstractUser

**Critérios de aceite — US14:**
- [ ] Lista de pedidos ordenada por data (mais recente primeiro)
- [ ] Cada pedido exibe protocolo, data, total e status
- [ ] Link para detalhe de cada pedido

---

### Épico 5 — Painel Administrativo

| ID | Como... | Quero... | Para... |
|---|---|---|---|
| US16 | Admin | Cadastrar e editar produtos com foto | Manter o cardápio atualizado |
| US17 | Admin | Gerenciar categorias | Organizar o catálogo |
| US18 | Admin | Ver todos os pedidos do dia com status | Controlar a produção |
| US19 | Admin | Atualizar o status de um pedido | Informar o cliente sobre o andamento |
| US20 | Admin | Ver dashboard com resumo do dia | Ter visão rápida do negócio |

**Critérios de aceite — US16:**
- [ ] Formulário de produto com upload de imagem funcional
- [ ] Campos de preço promocional aparecem ao marcar "Em promoção"
- [ ] Produto inativo não aparece no catálogo público

**Critérios de aceite — US18:**
- [ ] Listagem de pedidos filtrável por status e data
- [ ] Cada linha exibe: protocolo, cliente, total, modo de entrega, status
- [ ] Pedidos novos destacados visualmente

**Critérios de aceite — US20:**
- [ ] Cards com: total de pedidos hoje, receita do dia, pedidos pendentes, pedidos prontos
- [ ] Acesso restrito a usuários `is_staff = True`

---

## 11. Métricas de Sucesso

### 11.1 KPIs de Negócio

| KPI | Meta inicial | Como medir |
|---|---|---|
| Pedidos via plataforma por mês | ≥ 50 pedidos/mês | Contagem de `Order` com status ≠ cancelado |
| Taxa de conversão (visitante → pedido) | ≥ 15% | Sessões únicas / pedidos finalizados |
| Ticket médio por pedido | ≥ R$ 80,00 | Média de `Order.total` |
| Receita mensal registrada | Crescimento mês a mês | Soma de `Order.total` por mês |

### 11.2 KPIs de Produto

| KPI | Meta | Como medir |
|---|---|---|
| Tempo médio de checkout | < 3 minutos | Análise de fluxo (tempo entre acesso ao cart e confirmação) |
| Taxa de abandono de carrinho | < 40% | Carrinhos criados vs. pedidos finalizados |
| Produtos mais acessados | Top 5 por semana | Contagem de acessos à página de detalhe |

### 11.3 KPIs de Operação

| KPI | Meta | Como medir |
|---|---|---|
| Tempo de atualização de status | < 30 min após preparo | Diferença entre `created_at` e última atualização de status |
| Taxa de pedidos sem observações problemáticas | > 90% | Feedback manual da operação |
| Uptime da aplicação | > 99% | Monitoramento de disponibilidade |

---

## 12. Riscos e Mitigações

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R01 | Fluxo de e-mail não funcionar em produção | Média | Alto | Usar Mailtrap em dev; documentar config SMTP para produção |
| R02 | Upload de imagens sem tamanho limite causando lentidão | Média | Médio | Validar tamanho máximo no model (`Pillow`) e template |
| R03 | Sessão do carrinho expirar antes do checkout | Baixa | Médio | Configurar `SESSION_COOKIE_AGE` adequado (ex: 7 dias) |
| R04 | Admin sem permissão acessando dashboard customizado | Baixa | Alto | Mixins `LoginRequiredMixin` + verificação `is_staff` em todas as views do dashboard |
| R05 | SQLite não suportar concorrência em alta carga | Baixa (fase inicial) | Alto | Aceitável para MVP; migração para PostgreSQL planejada em sprint final |
| R06 | Imagens armazenadas localmente se perderem no deploy | Média | Alto | Documentar backup de `MEDIA_ROOT`; migração para S3 em sprint futuro |
| R07 | TailwindCSS via CDN em produção (sem purge) | Alta | Médio | Usar TailwindCSS CLI standalone com build e purge configurados |

---

## 13. Lista de Tarefas por Sprint

---

### Sprint 0 — Setup e Configuração do Projeto

#### Tarefa 0.1 — Estrutura inicial do projeto Django
- [ ] 0.1.1 Criar o ambiente virtual Python com `python -m venv .venv`
- [ ] 0.1.2 Instalar Django 5.x via pip e gerar `requirements.txt`
- [ ] 0.1.3 Criar projeto Django com `django-admin startproject confeitaria .`
- [ ] 0.1.4 Configurar `settings.py`: `LANGUAGE_CODE = 'pt-br'`, `TIME_ZONE = 'America/Sao_Paulo'`, `USE_I18N = True`
- [ ] 0.1.5 Configurar `MEDIA_ROOT`, `MEDIA_URL` e servir arquivos de mídia no `urls.py` principal em modo `DEBUG`
- [ ] 0.1.6 Configurar `STATIC_ROOT` e `STATICFILES_DIRS` para o TailwindCSS compilado
- [ ] 0.1.7 Instalar `python-decouple` e criar arquivo `.env` com `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- [ ] 0.1.8 Adicionar `.env` e `db.sqlite3` ao `.gitignore`
- [ ] 0.1.9 Criar estrutura de pastas: `templates/`, `static/`, `media/`

#### Tarefa 0.2 — Instalação e configuração do TailwindCSS
- [ ] 0.2.1 Baixar TailwindCSS CLI standalone (`.exe` ou binário) para a pasta do projeto
- [ ] 0.2.2 Criar arquivo `tailwind.config.js` com `content` apontando para todos os templates Django (`templates/**/*.html`)
- [ ] 0.2.3 Criar arquivo `static/src/input.css` com as diretivas `@tailwind base/components/utilities`
- [ ] 0.2.4 Compilar o CSS com `tailwindcss -i static/src/input.css -o static/css/output.css --watch` em desenvolvimento
- [ ] 0.2.5 Referenciar `static/css/output.css` no `base.html` via `{% static %}`

#### Tarefa 0.3 — Template base e layout global
- [ ] 0.3.1 Criar `templates/base.html` com estrutura HTML5, meta tags responsivas, link para CSS compilado e Google Fonts
- [ ] 0.3.2 Implementar navbar com gradiente rosa, logo, links de navegação e ícone de carrinho com contador
- [ ] 0.3.3 Implementar footer simples com nome da confeitaria, redes sociais e horário de funcionamento
- [ ] 0.3.4 Criar bloco `{% block content %}` e `{% block title %}` no `base.html`
- [ ] 0.3.5 Criar template parcial `templates/_messages.html` para mensagens Django (`django.contrib.messages`)

#### Tarefa 0.4 — Criação das apps Django
- [ ] 0.4.1 Criar app `core` com `python manage.py startapp core`
- [ ] 0.4.2 Criar app `catalog` com `python manage.py startapp catalog`
- [ ] 0.4.3 Criar app `cart` com `python manage.py startapp cart`
- [ ] 0.4.4 Criar app `orders` com `python manage.py startapp orders`
- [ ] 0.4.5 Criar app `accounts` com `python manage.py startapp accounts`
- [ ] 0.4.6 Criar app `dashboard` com `python manage.py startapp dashboard`
- [ ] 0.4.7 Registrar todas as apps em `INSTALLED_APPS` no `settings.py`
- [ ] 0.4.8 Criar `urls.py` em cada app e incluir no `urls.py` principal com prefixos adequados

#### Tarefa 0.5 — Model base abstrato
- [ ] 0.5.1 Criar arquivo `core/models.py` com model abstrato `TimeStampedModel` contendo `created_at = models.DateTimeField(auto_now_add=True)` e `updated_at = models.DateTimeField(auto_now=True)`
- [ ] 0.5.2 Documentar no `TimeStampedModel` que todos os models do projeto devem herdar dele

---

### Sprint 1 — Autenticação e Perfil de Usuário

#### Tarefa 1.1 — Model de usuário customizado
- [ ] 1.1.1 Criar model `CustomUser` em `accounts/models.py` herdando de `AbstractUser` e `TimeStampedModel`
- [ ] 1.1.2 Adicionar campo `phone = models.CharField(max_length=20, blank=True)` ao `CustomUser`
- [ ] 1.1.3 Definir `AUTH_USER_MODEL = 'accounts.CustomUser'` no `settings.py` **antes** da primeira migration
- [ ] 1.1.4 Executar `python manage.py makemigrations accounts` e `python manage.py migrate`

#### Tarefa 1.2 — Model de endereço
- [ ] 1.2.1 Criar model `Address` em `accounts/models.py` herdando de `TimeStampedModel`
- [ ] 1.2.2 Campos: `user (FK)`, `street`, `number`, `complement (blank)`, `neighborhood`, `city`, `state`, `zip_code`, `is_default (bool, default=False)`
- [ ] 1.2.3 Criar migration e migrar

#### Tarefa 1.3 — Formulários de autenticação
- [ ] 1.3.1 Criar `accounts/forms.py` com `RegisterForm` herdando de `UserCreationForm` com campos: `first_name`, `last_name`, `email`, `phone`, `password1`, `password2`
- [ ] 1.3.2 Criar `LoginForm` usando `AuthenticationForm` do Django
- [ ] 1.3.3 Criar `ProfileForm` para edição de perfil com campos: `first_name`, `last_name`, `phone`
- [ ] 1.3.4 Aplicar classes TailwindCSS nos widgets dos formulários via `django-widget-tweaks`

#### Tarefa 1.4 — Views de autenticação
- [ ] 1.4.1 Criar `RegisterView` (CBV `CreateView`) em `accounts/views.py` que autentica o usuário automaticamente após cadastro
- [ ] 1.4.2 Usar `LoginView` e `LogoutView` do `django.contrib.auth.views` configurados nas URLs
- [ ] 1.4.3 Criar `ProfileView` (CBV `UpdateView` com `LoginRequiredMixin`) para edição de dados do usuário
- [ ] 1.4.4 Configurar `LOGIN_REDIRECT_URL = 'core:home'` e `LOGOUT_REDIRECT_URL = 'core:home'` no `settings.py`

#### Tarefa 1.5 — Templates de autenticação
- [ ] 1.5.1 Criar `templates/accounts/register.html` com formulário estilizado, link para login
- [ ] 1.5.2 Criar `templates/accounts/login.html` com formulário estilizado, link para cadastro
- [ ] 1.5.3 Criar `templates/accounts/profile.html` com formulário de edição e seção de histórico de pedidos (link)
- [ ] 1.5.4 Atualizar navbar para exibir nome do usuário logado e link para perfil/logout, ou links de login/cadastro para visitantes

---

### Sprint 2 — Catálogo de Produtos

#### Tarefa 2.1 — Models de Catálogo
- [ ] 2.1.1 Criar model `Category` em `catalog/models.py` herdando de `TimeStampedModel`; campos: `name`, `slug (auto)`, `description`, `image`, `is_active`, `sort_order`
- [ ] 2.1.2 Criar model `Product` em `catalog/models.py` herdando de `TimeStampedModel`; campos: `category (FK)`, `name`, `slug (auto)`, `description`, `price`, `image`, `is_active`, `is_featured`, `is_promotion`, `promotion_price`, `stock`
- [ ] 2.1.3 Sobrescrever método `save()` para auto-gerar `slug` a partir do `name` com `slugify`
- [ ] 2.1.4 Adicionar `get_absolute_url()` ao model `Product` apontando para a view de detalhe
- [ ] 2.1.5 Adicionar propriedade `current_price` ao `Product` que retorna `promotion_price` se `is_promotion` else `price`
- [ ] 2.1.6 Registrar models no `catalog/admin.py` com `list_display`, `list_filter` e `search_fields` configurados
- [ ] 2.1.7 Executar `makemigrations catalog` e `migrate`

#### Tarefa 2.2 — Views do catálogo
- [ ] 2.2.1 Criar `ProductListView` (CBV `ListView`) em `catalog/views.py` com queryset `Product.objects.filter(is_active=True)`
- [ ] 2.2.2 Implementar filtragem por categoria via `get_queryset()` usando `self.request.GET.get('categoria')`
- [ ] 2.2.3 Implementar busca por nome via `get_queryset()` usando `self.request.GET.get('q')`
- [ ] 2.2.4 Passar lista de categorias ativas ao contexto via `get_context_data()` para o menu de filtros
- [ ] 2.2.5 Criar `ProductDetailView` (CBV `DetailView`) com `queryset = Product.objects.filter(is_active=True)` e `slug_field = 'slug'`
- [ ] 2.2.6 Configurar URLs em `catalog/urls.py`: `path('', ProductListView, name='list')` e `path('<slug:slug>/', ProductDetailView, name='detail')`

#### Tarefa 2.3 — Templates do catálogo
- [ ] 2.3.1 Criar `templates/catalog/product_list.html` estendendo `base.html`
- [ ] 2.3.2 Implementar barra de filtros por categoria (pills/tabs com TailwindCSS) e campo de busca
- [ ] 2.3.3 Implementar grid responsivo de cards de produto usando o padrão definido no Design System
- [ ] 2.3.4 Criar partial `templates/catalog/_product_card.html` reutilizável com badge de promoção e destaque
- [ ] 2.3.5 Criar `templates/catalog/product_detail.html` com imagem grande, nome, descrição, preço e botão "Adicionar ao carrinho"
- [ ] 2.3.6 Implementar estado vazio (nenhum produto encontrado) com mensagem amigável

#### Tarefa 2.4 — Página inicial (core)
- [ ] 2.4.1 Criar `HomeView` (CBV `TemplateView`) em `core/views.py` que passa ao contexto: produtos em destaque (top 4) e categorias ativas
- [ ] 2.4.2 Criar `templates/core/home.html` com seção hero (gradiente + chamada para ação), seção de destaques e seção de categorias
- [ ] 2.4.3 Configurar URL `path('', HomeView, name='home')` em `core/urls.py` e incluir no `urls.py` principal

---

### Sprint 3 — Carrinho de Compras

#### Tarefa 3.1 — Lógica do carrinho em sessão
- [ ] 3.1.1 Criar `cart/cart.py` com classe `Cart` que gerencia o carrinho na sessão Django
- [ ] 3.1.2 Implementar método `add(product, quantity=1)` que adiciona ou incrementa item na sessão
- [ ] 3.1.3 Implementar método `remove(product_id)` que remove item da sessão
- [ ] 3.1.4 Implementar método `update(product_id, quantity)` que atualiza a quantidade
- [ ] 3.1.5 Implementar propriedade `total` que soma `price * quantity` de todos os itens
- [ ] 3.1.6 Implementar método `__len__()` retornando a quantidade total de itens
- [ ] 3.1.7 Implementar método `__iter__()` que itera sobre itens enriquecendo com objetos `Product` do banco
- [ ] 3.1.8 Implementar método `clear()` para limpar o carrinho após pedido confirmado

#### Tarefa 3.2 — Context processor do carrinho
- [ ] 3.2.1 Criar `cart/context_processors.py` com função `cart` que injeta `cart_count` em todos os templates
- [ ] 3.2.2 Registrar o context processor em `settings.py` dentro de `TEMPLATES[0]['OPTIONS']['context_processors']`

#### Tarefa 3.3 — Views do carrinho
- [ ] 3.3.1 Criar `CartDetailView` (CBV `View`) em `cart/views.py` que renderiza o carrinho atual
- [ ] 3.3.2 Criar `CartAddView` (CBV `View`, método POST) que recebe `product_id` e `quantity` e adiciona ao carrinho, redirecionando com mensagem de sucesso
- [ ] 3.3.3 Criar `CartRemoveView` (CBV `View`, método POST) que remove item do carrinho
- [ ] 3.3.4 Criar `CartUpdateView` (CBV `View`, método POST) que atualiza quantidade de um item
- [ ] 3.3.5 Configurar URLs em `cart/urls.py`

#### Tarefa 3.4 — Templates do carrinho
- [ ] 3.4.1 Criar `templates/cart/detail.html` com tabela/lista de itens, colunas: produto, preço unitário, quantidade (inputs + / −), subtotal, ação remover
- [ ] 3.4.2 Implementar totalizador: subtotal, frete (campo fixo "A combinar") e total
- [ ] 3.4.3 Botão "Finalizar Pedido" levando ao checkout e botão "Continuar Comprando" voltando ao catálogo
- [ ] 3.4.4 Exibir estado vazio do carrinho com mensagem e link para o catálogo

---

### Sprint 4 — Checkout e Pedidos

#### Tarefa 4.1 — Models de pedido
- [ ] 4.1.1 Criar model `Order` em `orders/models.py` herdando de `TimeStampedModel` com todos os campos definidos no schema ER
- [ ] 4.1.2 Definir `STATUS_CHOICES` como tupla de constantes na própria model: `RECEIVED`, `PREPARING`, `READY`, `DELIVERED`
- [ ] 4.1.3 Definir `DELIVERY_CHOICES`: `PICKUP` (retirada) e `DELIVERY` (entrega)
- [ ] 4.1.4 Implementar método `generate_protocol()` que gera protocolo único (ex: `CON-{ano}{random 4 digitos}`) e chamá-lo no `save()` quando `protocol` estiver vazio
- [ ] 4.1.5 Criar model `OrderItem` em `orders/models.py` herdando de `TimeStampedModel` com campos: `order (FK)`, `product (FK null=True on_delete=SET_NULL)`, `product_name`, `unit_price`, `quantity`, `subtotal`
- [ ] 4.1.6 Implementar método `save()` no `OrderItem` para calcular `subtotal = unit_price * quantity` automaticamente
- [ ] 4.1.7 Registrar models no `orders/admin.py` com inline de `OrderItem` dentro de `Order`
- [ ] 4.1.8 Executar `makemigrations orders` e `migrate`

#### Tarefa 4.2 — Formulário de checkout
- [ ] 4.2.1 Criar `orders/forms.py` com `CheckoutForm` baseado em `forms.Form` (não ModelForm) com campos: `customer_name`, `customer_email`, `customer_phone`, `delivery_type` (RadioSelect), `delivery_address` (Textarea, required=False), `scheduled_at` (DateTimeInput), `notes` (Textarea, required=False)
- [ ] 4.2.2 Implementar validação `clean()` que exige `delivery_address` se `delivery_type == 'delivery'`
- [ ] 4.2.3 Aplicar classes TailwindCSS nos widgets via atributos `attrs` no `__init__` do formulário

#### Tarefa 4.3 — Views de checkout e pedido
- [ ] 4.3.1 Criar `CheckoutView` (CBV `FormView`) em `orders/views.py` que renderiza o formulário de checkout
- [ ] 4.3.2 No método `get_initial()`, pré-preencher dados do cliente logado se `request.user.is_authenticated`
- [ ] 4.3.3 No método `form_valid()`: criar `Order`, criar `OrderItem` para cada item do carrinho, chamar `cart.clear()`, disparar e-mail de confirmação e redirecionar para página de sucesso
- [ ] 4.3.4 Criar `OrderSuccessView` (CBV `DetailView`) que exibe página de confirmação com protocolo, buscando a `Order` pelo `pk` ou `protocol`
- [ ] 4.3.5 Criar `OrderHistoryView` (CBV `ListView` com `LoginRequiredMixin`) que lista pedidos do usuário logado ordenados por `-created_at`
- [ ] 4.3.6 Criar `OrderDetailView` (CBV `DetailView` com `LoginRequiredMixin`) que exibe detalhe de um pedido do usuário logado (verificar `order.user == request.user`)
- [ ] 4.3.7 Configurar URLs em `orders/urls.py`

#### Tarefa 4.4 — Templates de checkout e pedido
- [ ] 4.4.1 Criar `templates/orders/checkout.html` com formulário em duas colunas (dados do cliente | resumo do pedido)
- [ ] 4.4.2 Implementar toggle JS vanilla para mostrar/ocultar campo de endereço conforme seleção de `delivery_type`
- [ ] 4.4.3 Criar `templates/orders/order_success.html` com card de confirmação: protocolo em destaque, lista de itens, total, mensagem de agradecimento e link para home
- [ ] 4.4.4 Criar `templates/orders/order_history.html` com tabela de pedidos: protocolo, data, total, status (badge colorido), link "Ver detalhe"
- [ ] 4.4.5 Criar `templates/orders/order_detail.html` com detalhe completo do pedido: dados do cliente, itens, endereço de entrega, observações e status atual

#### Tarefa 4.5 — E-mail de confirmação de pedido
- [ ] 4.5.1 Criar `orders/signals.py` com signal `post_save` no model `Order` que dispara e-mail de confirmação ao cliente quando `created=True`
- [ ] 4.5.2 Conectar signal no `orders/apps.py` via método `ready()`
- [ ] 4.5.3 Criar template de e-mail `templates/orders/email/order_confirmation.html` com dados do pedido formatados
- [ ] 4.5.4 Criar template de e-mail texto puro `templates/orders/email/order_confirmation.txt`
- [ ] 4.5.5 Configurar `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` em desenvolvimento no `settings.py`

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

---

*Documento gerado em: 27/04/2026*  
*Versão: 1.0*
