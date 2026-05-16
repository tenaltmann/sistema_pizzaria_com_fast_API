# 🍕 Sistema de Pizzaria com FastAPI

Sistema backend para gerenciamento de pedidos de pizzaria desenvolvido com FastAPI, utilizando autenticação JWT, integração com banco de dados relacional via SQLAlchemy e estrutura modular baseada em rotas.

Repositório oficial:
[https://github.com/tenaltmann/sistema_pizzaria_com_fast_API](https://github.com/tenaltmann/sistema_pizzaria_com_fast_API)

---

## 🚀 Tecnologias Utilizadas

* Python 3.12+
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* JWT Authentication
* Passlib + Bcrypt
* Uvicorn

---

## 📂 Estrutura Atual do Projeto

```bash
sistema_pizzaria_com_fast_API/
│
├── main.py                 # Inicialização da aplicação
├── models.py               # Modelos do banco de dados
├── schemas.py              # Schemas Pydantic
├── database.py             # Configuração do banco
├── dependencies.py         # Dependências reutilizáveis
├── auth_routes.py          # Rotas de autenticação
├── pedido_routes.py        # Rotas de pedidos
├── requirements.txt
├── .env
│
├── venv/
└── __pycache__/
```

---

## 🔐 Funcionalidades Implementadas

### 👤 Autenticação

* Cadastro de usuários
* Login com JWT
* Geração de token de acesso
* Proteção de rotas autenticadas
* Hash de senha com Bcrypt

---

### 🍕 Pedidos

* Criação de pedidos
* Listagem de pedidos
* Relacionamento entre usuários e pedidos
* Persistência em banco de dados

---

### 🗄️ Banco de Dados

* Integração com SQLAlchemy ORM
* Sessões reutilizáveis
* Criação automática das tabelas
* Estrutura preparada para migração futura

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/tenaltmann/sistema_pizzaria_com_fast_API.git
```

---

### 2️⃣ Acesse a pasta

```bash
cd sistema_pizzaria_com_fast_API
```

---

### 3️⃣ Crie o ambiente virtual

### Windows

```bash
python -m venv venv
```

Ative:

```bash
venv\Scripts\activate
```

---

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Execute o servidor

```bash
uvicorn main:app --reload
```

---

## 📌 Acesse a documentação automática

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

Redoc:

```bash
http://127.0.0.1:8000/redoc
```

---

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📖 Conceitos Aplicados no Projeto

* API REST
* CRUD
* JWT Authentication
* Dependency Injection
* ORM
* Serialização com Pydantic
* Organização modular com rotas
* Segurança de autenticação
* Relações entre tabelas

---

## 🎯 Objetivo do Projeto

Este proj
