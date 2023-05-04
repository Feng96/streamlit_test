import streamlit as st
import leafmap.foliumap as leafmap


st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

options= list(leafmap.basemaps.keys())

m  = leafmap.Map()


with col2:
    dropdown = st.selectbox('Basenap', options)
    default_urls = leafmap.basemaps[dropdown].tiles
    url =st.text_input('URL',value=default_urls)

m.add_basemap(dropdown)

if url:
    m.add_tile_layer(url, name='Tile Layer', attribution='Tile Layer')

with col1:
    m.to_streamlit()

