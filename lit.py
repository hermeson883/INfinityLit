import streamlit as st
import pandas as pd

# Colocando o titulo da minha página (equivalente ao H1 do HTML)
st.title("Hello world")
st.write("""
    Primeira página com streamlit
""", unsafe_allow_html=True)


#Leitura de imagem com o streamlit
st.image("https://images.unsplash.com/photo-1603676671615-12e7cc7d9cad?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ODBzfGVufDB8fDB8fHww")


# Escrevendo algo no formato markdown
st.write(""" # Suba seu arquivo bem aqui """)

#Lendo um arquivo com o streamlit e falando qual os tipos de arquivo ele aceita
arquivo = st.file_uploader("Suba o seu arquivo", type=['csv', "png", "json"])

#Vendo se existe algo dentro dessa variável
if arquivo:
#Lendo arquivos em formato csv e json
    if "csv" in arquivo.type:
        print(arquivo.type)
        df = pd.read_csv(arquivo, sep=',')
        st.dataframe(df)
    elif "json" in arquivo.type:
        print(arquivo.type)
        df = pd.read_json(arquivo)
        st.write(df)


# Campo de input
numero = st.text_input('Digite sua idade')

# Criando a sidebar
barraLateral = st.sidebar


