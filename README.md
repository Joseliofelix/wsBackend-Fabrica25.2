# LojaFake API 🛒

API de loja online fake construída com **Django** e **Django REST Framework**.  
Permite gerenciar **categorias**, **produtos** e importar produtos automaticamente da **Fake Store API**.

-----------------------------------------------------------------------------------

## 💻 Tecnologias utilizadas

- Python 3.13.1 
- Django 5.2.6  
- Django REST Framework  
- Requests (para integração com API externa)  
- SQLite (banco de dados padrão, sem configuração externa)

-----------------------------------------------------------------------------------

## 🔧 Funcionalidades

- **Categorias**: CRUD (`/api/categorias/`)  
- **Produtos**: CRUD (`/api/produtos/`)  
- **Importação automática** de produtos da Fake Store API (`/api/importar/`)

-----------------------------------------------------------------------------------

## 📁 Estrutura do projeto

```text
Projeto/
├─ produtos/
│ ├─ models.py      # Modelos Categoria e Produto
│ ├─ serializers.py # Serializers para API
│ ├─ views.py       # ViewSets e endpoint de importação
│ ├─ urls.py        # Rotas da app produtos
│ └─ services.py    # Lógica para importar produtos
├─ Projeto/
│ └─ urls.py        # Rotas do projeto
├─ manage.py
```
-----------------------------------------------------------------------------------

## ⚙️ Instalação e execução

### 1. Clone o repositório (ou abra a pasta do projeto)

```bash
git clone < https://github.com/Joseliofelix/wsBackend-Fabrica25.2 >
cd LojaFake
```
### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv # Windows
venv\Scripts\activate 
source venv/bin/activate # Linux / Mac
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Rode as migrations
```bash
python manage.py migrate
```
### 5. Crie um superusuário (opcional, para acessar o admin)
```bash
python manage.py createsuperuser
```
### 6. Execute o servidor
```bash
python manage.py runserver
A API estará disponível em http://127.0.0.1:8000/
```

## 🌐 Endpoints da API

Endpoint	                Método	                            Descrição

`/api/categorias/`	      GET / POST	        Lista todas as categorias ou cria uma nova categoria.
`/api/categorias/{id}/`	  GET / PUT /DELETE	    Ver detalhes, atualiza ou deleta uma categoria específica.
`/api/produtos/`	      GET / POST	        Lista todos os produtos ou cria um novo produto.
`/api/produtos/{id}/`	  GET / PUT /DELETE	    Ver detalhes, atualiza ou deleta um produto específico.
`/api/importar/`	         POST	            Importa produtos da Fake Store API automaticamente.

## 💡 Você pode acessar os endpoints diretamente no navegador.

Para `/api/importar/,`  #os produtos serão importados ou atualizados automaticamente.


## 📌 Exemplos de uso

Listar produtos:

`http://127.0.0.1:8000/api/produtos/`

Listar categorias:

`http://127.0.0.1:8000/api/categorias/`

Importar produtos:

`http://127.0.0.1:8000/api/importar/`

Retorno esperado ao importar produtos:

```json
{"mensagem": "20 produtos importados da Fake Store API"}
```
## 📝 Observações importantes

O banco de dados padrão é SQLite, então não é necessário configurar nenhum banco externo.
O superusuário é opcional, mas ele permite acessar o painel administrativo:

`http://127.0.0.1:8000/admin/`

Todos os endpoints podem ser testados diretamente no navegador ou com ferramentas como curl ou Postman.