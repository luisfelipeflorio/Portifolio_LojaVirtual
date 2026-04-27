# Agentes de IA — Confeitaria Virtual

Agentes especializados na stack do projeto (Django 5.x · TailwindCSS 3.x · Python 3.12).

---

## Agentes

| Arquivo | Agente | Quando usar |
|---|---|---|
| [backend.md](backend.md) | Django Backend Engineer | Models, migrations, views, forms, URLs, signals, admin, cart, autenticação |
| [frontend.md](frontend.md) | Frontend Engineer | Templates HTML, TailwindCSS, design system, componentes, responsividade |
| [qa.md](qa.md) | QA Engineer | Testar fluxos no browser, validar design e comportamento real da aplicação |

---

## Como usar

Cada agente é um arquivo `.md` que pode ser invocado como sub-agente no Claude Code:

```
claude --agent agents/backend.md "Implemente a view de checkout"
```

Ou referenciado diretamente na conversa com `@agents/backend.md`.

---

## Divisão de responsabilidades

```
Backend  →  lógica de negócio, dados, servidor
Frontend →  apresentação, templates, estilos
QA       →  validação do produto funcionando no browser
```

Os agentes de backend e frontend usam o **MCP Context7** para consultar documentação atualizada das bibliotecas. O agente de QA usa o **MCP Playwright** para interagir com o servidor Django em execução.
