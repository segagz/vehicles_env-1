import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv('vehicles_us.csv')
st.header('Escoge como quieres visualizar los datos de anuncios de venta de coches')
build_histogram = st.checkbox('Construir un histograma')
build_disp = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
            
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.histogram(car_data, x="odometer")
        
    st.plotly_chart(fig, use_container_width=True)


if build_disp: 
            
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.scatter(car_data, x="odometer", y="price")
        
    st.plotly_chart(fig, use_container_width=True)
