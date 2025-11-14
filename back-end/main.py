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


@app.put("/produtos/{id_produto}")
def atualizar_produtos(id_produto: int, novo_preco: float, nova_quantidade: int):
    produto = function.buscar_produto(id_produto)

    if produto:
        function.atualizar_produto(id_produto, novo_preco, nova_quantidade)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}
    
@app.delete("/produtos/{id_produto}")
def deletar_produtos(id_produto: int):
    produto = function.buscar_produto(id_produto)

    if produto:
        function.deletar_produto(id_produto)
        return {"mensagem": "Produto excluído com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}