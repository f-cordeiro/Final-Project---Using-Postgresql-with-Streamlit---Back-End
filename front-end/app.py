import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerência de Produtos", layout="wide")
st.title("® Hype Almoxarifado")

menu = st.sidebar.selectbox(
    "Menu",
    ["Listar Produtos", "Cadastrar Produto", "Atualizar Produto", "Deletar Produto"]
)
