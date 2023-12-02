import pandas as pd
import streamlit as st 

def tratar_ano(x):
    remove_comma = str(x)
    remove_comma.replace(',', '')
    return remove_comma


st.title("Hello world")

df = pd.read_csv("Players.csv")


df['born'] = df["born"].apply(tratar_ano)

st.write(df)

###################### Layout ################################
bar = st.sidebar

bar.selectbox(
    "# Bem vindo a sua área de trabalho",
    ['dsfs','sdxgdf']
)

bar.slider(
    "Select a range",
    0, 100
)


############################# Criando a barra lateral #################################
# Para criar a barra lateral temos que fazer uma pasta chamada "paste"

arquivo = st.file_uploader("Click aqui para upar o arquivo", type=["csv"])


# Vendo se a palavra csv existe nos tipos de arquivos que o streamlit aceita
if arquivo:
    if "csv" in arquivo.type:
        df = pd.read_csv(arquivo)
        st.write(df)

valores_unicos = df.columns

st.write(valores_unicos)

# Plotando um gráfico com streamlit
st.bar_chart(df["weight"])


    # Upando varios arquivos de uma vez:
st.write(arquivo)
for i in arquivo:
    if "csv" in i.type:
        df = pd.read_csv(i)
        st.write(df)




if arquivo:
    if 'csv' in arquivo.type:
        df = pd.read_csv(arquivo)
        st.write(df)

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
numero = st.text_input('Digite sua idade', )

