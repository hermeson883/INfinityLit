import streamlit as st
import pandas as pd

st.title("Data Visualization :chart_with_upwards_trend:")

user_file = st.file_uploader("Insira o seu arquivo aqui :point_down:", type=["csv", "xlsx"])

if user_file != None:
    st.dataframe(pd.read_csv(user_file, sep=";"))
    
