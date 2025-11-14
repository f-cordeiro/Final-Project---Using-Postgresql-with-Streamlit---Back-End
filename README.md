# Sistema de estoque para Almoxarifado
## Funções Aplicadas no Sistema (CRUD)
- Adicionar Produtos
- Listar Produtos
- Atualizar Produtos (Preço e Quantidade)
- Excluir Produtos
- Buscar Produtos da Tabela

# Crie Um Arquivo .env Para Armazenar as informações do seu DB
## Exemplo:
```
DB_NAME= "nome_db"
DB_USER= "nome_user"
DB_PASSWORD= "sua senha"
DB_HOST="seu local host"
DB_PORT="sua porta"
````

# Como Baixar os Arquivos Necessários
Entre no .venv pelo GitBash

- Instale os requirements.txt no terminal Bash
```
pip install -r requirements.txt
```

# Rodando a API
Entre pelo GitBash
- Rode o main.py dentro da pasta back-end, localizado dentro da .venv
- Utilize o comando:

```
cd back-end/
```
- Logo em seguida Rode o  arquivo main.py

```
uvicorn main:app --reload
```

# Rodando o Streamlit
Entre pelo GitBash
- Entre na pasta front-end
- utilize o comando:

```
cd front-end/
```

- rode o app.py dentro da pasta front-end


- utilize o comando:
```
python -m streamlit run app.py