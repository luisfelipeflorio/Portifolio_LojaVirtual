# Design System

Interface mobile-first em português brasileiro, com identidade visual de confeitaria artesanal.

---

## Tipografia

Fontes carregadas via Google Fonts no `base.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

| Uso | Fonte | Classes Tailwind |
|---|---|---|
| Títulos de página | Playfair Display | `font-['Playfair_Display'] text-3xl md:text-4xl font-bold text-neutral-900` |
| Títulos de seção | Playfair Display | `font-['Playfair_Display'] text-2xl font-semibold text-neutral-800` |
| Texto corpo | Inter | `font-['Inter'] text-base text-neutral-600 leading-relaxed` |
| Labels / captions | Inter | `font-['Inter'] text-sm font-medium text-neutral-500` |

---

## Paleta de Cores

| Token | Hex | Uso |
|---|---|---|
| `rose-50` | `#FFF1F3` | Fundos suaves |
| `rose-100` | `#FFE4E8` | Cards, hover suave |
| `rose-400` | `#FB7185` | Destaques, badges |
| `rose-500` | `#F43F5E` | Botão primário, links ativos |
| `rose-600` | `#E11D48` | Hover botão primário |
| `amber-400` | `#FBBF24` | Badges de promoção, ícones |
| `amber-500` | `#F59E0B` | Destaque premium |
| `stone-600` | `#57534E` | Texto corpo |
| `stone-900` | `#1C1917` | Títulos |
| `stone-50` | `#FAFAF9` | Background geral |
| `stone-100` | `#F5F5F4` | Background de seções |

---

## Gradientes

```html
<!-- Hero principal -->
<div class="bg-gradient-to-br from-rose-50 via-pink-100 to-rose-200">

<!-- Navbar -->
<nav class="bg-gradient-to-r from-rose-700 via-pink-600 to-rose-500">

<!-- Botão primário -->
<button class="bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-600 hover:to-pink-700">

<!-- Card destaque -->
<div class="bg-gradient-to-br from-amber-50 to-rose-50">
```

---

## Botões

```html
<!-- Primário -->
<button class="bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-600 hover:to-pink-700
               text-white font-medium px-6 py-3 rounded-xl shadow-md
               hover:shadow-lg transition-all duration-200 cursor-pointer">

<!-- Secundário (outline) -->
<button class="border-2 border-rose-500 text-rose-600 hover:bg-rose-50
               font-medium px-6 py-3 rounded-xl transition-all duration-200 cursor-pointer">

<!-- Ghost -->
<button class="text-rose-600 hover:text-rose-700 hover:bg-rose-50
               font-medium px-4 py-2 rounded-lg transition-all duration-200 cursor-pointer">

<!-- Perigo -->
<button class="bg-red-500 hover:bg-red-600 text-white
               font-medium px-4 py-2 rounded-lg transition-all duration-200 cursor-pointer">

<!-- Admin -->
<button class="bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-500 hover:to-amber-600
               text-white font-medium px-5 py-2.5 rounded-lg shadow-sm
               transition-all duration-200 cursor-pointer">
```

---

## Inputs e Formulários

```html
<!-- Input padrão -->
<input type="text"
       class="w-full px-4 py-3 rounded-xl border border-neutral-200
              bg-white focus:outline-none focus:ring-2 focus:ring-rose-400
              focus:border-transparent placeholder-neutral-400
              text-neutral-800 transition-all duration-200">

<!-- Input com erro -->
<input type="text"
       class="w-full px-4 py-3 rounded-xl border border-red-400
              bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-400
              text-neutral-800 transition-all duration-200">
<span class="text-xs text-red-500 mt-1">Mensagem de erro.</span>

<!-- Select -->
<select class="w-full px-4 py-3 rounded-xl border border-neutral-200
               bg-white focus:outline-none focus:ring-2 focus:ring-rose-400
               text-neutral-800 cursor-pointer transition-all duration-200">

<!-- Textarea -->
<textarea rows="4"
          class="w-full px-4 py-3 rounded-xl border border-neutral-200
                 bg-white focus:outline-none focus:ring-2 focus:ring-rose-400
                 text-neutral-800 resize-none transition-all duration-200">
```

---

## Card de Produto

```html
<div class="bg-white rounded-2xl shadow-sm hover:shadow-md border border-neutral-100
            overflow-hidden transition-all duration-200 group">
  <div class="relative overflow-hidden">
    <img src="..." alt="..."
         class="w-full h-52 object-cover group-hover:scale-105 transition-transform duration-300">
    <!-- Badge promoção -->
    <span class="absolute top-3 left-3 bg-amber-400 text-white text-xs font-semibold px-2 py-1 rounded-full">
      Promoção
    </span>
    <!-- Badge destaque -->
    <span class="absolute top-3 right-3 bg-rose-500 text-white text-xs font-semibold px-2 py-1 rounded-full">
      Destaque
    </span>
  </div>
  <div class="p-4">
    <h3 class="font-['Playfair_Display'] font-semibold text-neutral-900 text-lg">Nome</h3>
    <p class="text-sm text-neutral-500 mt-1 line-clamp-2">Descrição</p>
    <div class="flex items-center justify-between mt-4">
      <span class="text-rose-600 font-bold text-xl">R$ 0,00</span>
      <button class="bg-gradient-to-r from-rose-500 to-pink-600 text-white
                     text-sm font-medium px-4 py-2 rounded-xl hover:shadow-md
                     transition-all duration-200 cursor-pointer">
        Adicionar
      </button>
    </div>
  </div>
</div>
```

---

## Grid de Produtos

```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  {% for product in products %}
    {% include 'catalog/_product_card.html' %}
  {% endfor %}
</div>
```

---

## Badges de Status de Pedido

```html
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

## Navbar

```html
<nav class="bg-gradient-to-r from-rose-700 via-pink-600 to-rose-500 shadow-lg sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <a href="{% url 'core:home' %}" class="font-['Playfair_Display'] text-white text-2xl font-bold">
        Confeitaria
      </a>
      <div class="hidden md:flex items-center gap-6">
        <a href="{% url 'catalog:list' %}" class="text-rose-100 hover:text-white font-medium transition-colors">
          Cardápio
        </a>
        <a href="{% url 'cart:detail' %}" class="relative text-white">
          <!-- ícone carrinho -->
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
