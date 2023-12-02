# import streamlit as st
# import pandas as pd

# st.title("Minha primeira página :alien:")


# arquivo = st.file_uploader("Clique aqui para selecionar seu arquivo", type=["csv"])


# if arquivo:
#     if "csv" in arquivo.type:
#         data = pd.read_csv(arquivo)
#         st.write(data)

# cidades_unicas = df["birth_state"].dropna()

# cidades_unicas = cidades_unicas.unique()

# opcao = st.selectbox("Você deseja filtrar por qual cidade", ["fortaleza", "salvador", "recife"])

# filtrar = st.button("filtrar por cidade")

# if filtrar:
#     df_filtrado = df.loc[df["cidade"] == opcao]
#     st.dataframe(df_filtrado)

# button = st.button("Filtra")

# if button:
#     filtro = df[df["birth_state"] == selecao]
#     st.dataframe(filtro)
#     button_grafico = st.button("Deseja fazer um gráfico?")


import streamlit as st
import pandas as pd

st.title("Gráficos :bar_chart:")

arquivo = st.file_uploader("Suba seu arquivo bem aqui")

if arquivo is not None:
    df = pd.read_csv(arquivo, sep=",")
    df["DATE"] = pd.to_datetime(df["DATE"], format='%Y-%m-%d')
    st.write(df)
    st.write(df.dtypes)