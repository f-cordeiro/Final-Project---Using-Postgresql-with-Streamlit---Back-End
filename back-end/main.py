from fastapi import FastAPI
import function

app = FastAPI(title="Gerência de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo á gerencia de produtos"}

@app.post("/produtos")
def criar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    function.cadastrar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto cadastrado com sucesso!"}