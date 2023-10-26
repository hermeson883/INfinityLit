import streamlit as st
import pandas as pd

# Colocando o titulo da minha página (equivalente ao H1 do HTML)
st.title("Hello world")
st.write("Minha primeira página com streamlit")


#Leitura de imagem com o streamlit
st.image("https://images.unsplash.com/photo-1603676671615-12e7cc7d9cad?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ODBzfGVufDB8fDB8fHww")


# Escrevendo algo no formato markdown
st.write(""" # Suba seu arquivo bem aqui """)

#Lendo um arquivo com o streamlit e falando qual os tipos de arquivo ele aceita
arquivo = st.file_uploader("Suba o seu arquivo", type=['csv', "png", "json"])

#Lendo arquivos em formato csv e json
if "csv" in arquivo.type:
    print(arquivo.type)
    dataframe = pd.read_csv(arquivo, sep=';')
    st.write(dataframe)
elif "json" in arquivo.type:
    print(arquivo.type)
    df = pd.read_json(arquivo)
    st.write(df)