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