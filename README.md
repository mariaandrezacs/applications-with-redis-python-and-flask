# Flask + Redis (Starter Kit)

Este projeto é um starter kit educativo que demonstra como estruturar uma aplicação web em Python usando **Flask**, com integração a **Redis** (para cache/armazenamento em memória) e um repositório SQLite de exemplo. O foco é oferecer uma base simples, modular e fácil de estender para aprender padrões de composição, repositórios e roteamento.

---

**Funcionalidades principais**
- API REST mínima para gerenciamento de produtos (criação e busca por nome).
- Exemplo de composição de serviços e separação entre adaptadores (Redis/SQLite) e camadas de aplicação.
- Estrutura de pastas pensada para ensino e extensão rápida.

---


**Requisitos**
- Python 3.10+
- Redis (opcional para testes de cache; sem Redis a aplicação pode funcionar somente com o repositório SQLite)

Instale dependências:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
```

---


**Executando a aplicação**

```bash
python run.py
```

Por padrão o servidor inicia na porta configurada em `src/main/server/server_settings.py`.

---

**Endpoints (exemplos)**
- Criar produto (POST /products)

```bash
curl -X POST http://localhost:5000/products \
	-H "Content-Type: application/json" \
	-d '{"name": "caneta", "price": 2.5}'
```

- Buscar produto por nome (GET /products/<product_name>)

```bash
curl http://localhost:5000/products/caneta
```

Os handlers estão em `src/main/routes/products_routes.py`.

---

**Como contribuir / próximos passos**
- Adicionar testes automatizados para as rotas e repositórios.
- Implementar integração contínua (CI) para lint e testes.
- Expandir os exemplos de uso do Redis (expiração, pub/sub, locks).

---
