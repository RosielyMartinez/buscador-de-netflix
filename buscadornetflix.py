import streamlit as st
import pandas as pd

@st.cache_data
def load_data(nrows=500):
    return pd.read_csv('movies.csv', nrows=nrows)

st.title('Netflix app')
data = load_data(500)
st.text('Done! (using st.cache)')

show_all = st.sidebar.checkbox('Mostrar todos los filmes')

title_input = st.sidebar.text_input('Titulo del filme:')
btn_search_title = st.sidebar.button('Buscar filmes')

directors_list = data['director'].dropna().unique()
selected_director = st.sidebar.selectbox('Seleccionar Director', directors_list)
btn_filter_director = st.sidebar.button('Filtrar director')

if btn_search_title:
    if title_input:
        filtered_by_title = data[data['name'].str.contains(title_input, case=False, na=False)]
        st.write(f'Total filmes mostrados: {len(filtered_by_title)}')
        st.dataframe(filtered_by_title)
    else:
        st.warning('Ingresa un título para buscar.')

elif btn_filter_director:
    filtered_by_director = data[data['director'] == selected_director]
    st.write(f'Total filmes : {len(filtered_by_director)}')
    st.dataframe(filtered_by_director)

elif show_all:
    st.subheader('Todos los filmes')
    st.dataframe(data)
