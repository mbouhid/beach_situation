# Libs
import sqlite3
import streamlit as st
import calendar
import pandas as pd


# Tab Title
st.set_page_config(
    page_title='Cadastro das Praias',
    page_icon='🏄‍♂️',
    layout='wide')

# Page Title
st.title('Cadastro das Praias')


# Connect DB
conn = sqlite3.connect('beaches.db', check_same_thread=False)
cur = conn.cursor()


def form():
    st.write('Preencher com as informações das Praias')
    with st.form(key='Cadstro das Praias', clear_on_submit=True):
        beach_name = st.text_input('Nome da Praia:')
        lat = st.text_input('Latidute:')
        lon = st.text_input('Longitude:')
                
        submission = st.form_submit_button(label='Salvar')
        #clear = st.form_submit_button(label='Limpar')
        if submission == True:
            addData(beach_name, lat, lon)
            st.success('Guardado com sucesso!')
            #if clear == True:
            #    st.sidebar.success('Limpeza feita!')


def addData(a, b, c):
    cur.execute("""CREATE TABLE IF NOT EXISTS beaches(
                beach_name TEXT(20),
                lat REAL(4),
                lon REAL(4));
                """)
    cur.execute("INSERT INTO beaches VALUES (?,?,?)", (a, b, c))
    conn.commit()
    #st.success('Successfully submitted')


form()


# Verificação da tabela criada
#query = """
#    select * from request
#    
#"""
#df = pd.read_sql_query(query, conn)
#st.write(df)

## Filters
#st.sidebar.multiselect(
#    'Escolha um produto',
#    list(df['nome_produto'].unique()), 
#    default=list(df['nome_produto'].unique())
#)
#
#st.sidebar.multiselect(
#    'Escolha os meses',
#    months, 
#)


#df['qtd'] = df['qtd'].astype(int)
#df_filtered = df[df['nome_produto'] == 'test2']
#texto = 'A soma do test2 é : '
#st.write(texto, df_filtered['qtd'].sum())

conn.close()