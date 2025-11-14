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

@app.get("/produtos")
def listar_produtos():
    produtos = function.listar_produto()
    lista = []

    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
    
    return {"produtos": lista}