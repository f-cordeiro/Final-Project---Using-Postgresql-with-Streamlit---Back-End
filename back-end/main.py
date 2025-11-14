from fastapi import FastAPI
import function

app = FastAPI(title="Gerência de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo á gerencia de produtos"}