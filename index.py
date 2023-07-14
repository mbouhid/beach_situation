# Libraries
import sqlite3
import calendar
import pandas as pd
from PIL import Image
import streamlit as st
from get_weather import get_weather
import plotly.express as px
import plotly.graph_objects as go
import pyarrow as pa


# Tab Title
st.set_page_config(
    page_title='Beach Situation',
    page_icon='🏄‍♂️',
    layout='wide')

# Page Title
st.header('BEACHES')


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

beach_name = ', '.join(df['beach_name'].values).title()
lat = ', '.join(str(num) for num in df['lat'].values)
lon = ', '.join(str(num) for num in df['lon'].values)

busca_dados = get_weather(beach_name, lat, lon)

st.table(busca_dados)


st.sidebar.write("---")

with st.container():

    result = pd.DataFrame.from_dict([busca_dados])
    result.set_index('Code', inplace=True)


    fig = px.scatter_mapbox(
        #fixed_result,
        result,
        hover_name="Nome da Praia",
        hover_data={
            "Nome da Praia": True,
            "Região": True,
            "Temperatura (ºC)": True,
            "Velocidade do Vento (km/h)": True,
            "Condição Climática": True,
        },
        zoom=14,
        lat="latitude",
        lon="longitude"
    )
    fig.update_traces(
        marker=dict(
            size=12,
            color="red"
        )
    )

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st.plotly_chart(fig)