import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerência de Produtos", layout="wide")
st.title("® Hype Almoxarifado")

menu = st.sidebar.selectbox(
    "Menu",
    ["Listar Produtos", "Cadastrar Produto", "Atualizar Produto", "Deletar Produto"]
)


if menu == "Listar Produtos":
    st.subheader("Estoque ☑ ")

    response = requests.get(f"{API_URL}/produtos")

    if response.status_code == 200:
        produtos = response.json().get("produtos", [])

        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado ainda!, Tente Novamente !")
    else:
        st.error("Erro ao conectar com a API.")

elif menu == "Cadastrar Produto":
    st.header("Bem - Vindo a Área de Cadastro de Produtos!")
    st.subheader("✔ Cadastrar Novo Produto")

    nome= st.text_input("Nome")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade", min_value=0, step=1)

    if st.button("Cadastrar Produto ✅"):
        if nome and categoria:
            params = {
                "nome": nome,
                "categoria": categoria,
                "preco": preco,
                "quantidade": quantidade,
            }

            response= requests.post(f"{API_URL}/produtos", params=params)

            if response.status_code == 200:
                st.success("Produto cadastrado com sucesso!")
            else:
                st.error("Erro ao cadastrar produto")
        else:
            st.warning("Preencha todos os campos obrigatórios")