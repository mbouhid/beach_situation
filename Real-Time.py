# Libraries
import sqlite3
import calendar
import pandas as pd
from PIL import Image
import streamlit as st
from get_weather import get_weather


# Tab Title
st.set_page_config(
    page_title='Beach Situation',
    page_icon='🏄‍♂️',
    layout='wide')




# Connect DB
conn = sqlite3.connect('beaches.db', check_same_thread=False)
cur = conn.cursor()

query = """
    select * from beaches
"""
df = pd.read_sql_query(query, conn)
conn.close()

### BARRA LATERAL ###

st.sidebar.markdown( '## Filtros' )

praia = st.sidebar.selectbox(
    'Search',
    list(df['beach_name'].unique()))

# praias = st.sidebar.multiselect(
#     'Search beach name:',
#     list(df['beach_name'].unique()),
#     'Praia de Matosinhos')
linhas_selecionadas = df['beach_name'].isin([praia])
df = df.loc[linhas_selecionadas, :]
#df.columns = ['Nome da Praia', 'Latitude', 'Longitude']




#st.text(', '.join(df['Nome da Praia'].values).title())
#st.text(', '.join(str(num) for num in df['Latitude'].values))
#st.text(', '.join(str(num) for num in df['Latitude'].values))

#beach_name = ', '.join(df['Nome da Praia'].values).title()
lat = ', '.join(str(num) for num in df['lat'].values)
lon = ', '.join(str(num) for num in df['lon'].values)

busca_dados = get_weather(lat, lon)
#busca_dados = get_weather()




st.sidebar.write("---")


# ### FILTRO POR MÊS ###
# mes = st.sidebar.multiselect(
#     "Selecione os Meses:",
#     options=list(df["mes_entrega"].unique()),
#     default=list(df["mes_entrega"].unique()))
# linhas_selecionadas = df['mes_entrega'].isin(mes)
# df = df.loc[linhas_selecionadas, :]

# ### FILTRO POR CLIENTE ###
# clientes = st.sidebar.multiselect(
#     "Selecione os clientes:",
#     options=list(df["nome_cliente"].unique()),
#     default=list(df["nome_cliente"].unique()))
# linhas_selecionadas = df['nome_cliente'].isin(clientes)
# df = df.loc[linhas_selecionadas, :]


# Page Title
st.header('BEACHES')


st.table(busca_dados)

