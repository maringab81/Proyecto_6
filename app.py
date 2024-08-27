import pandas as pd
import streamlit as st
import plotly.express as px 


vehicles_us = pd.read_csv("vehicles_us.csv")

st.header('Precio de autos')

build_histogram = st.checkbox('Construir un histograma') # crear un botón
        
if build_histogram: # al hacer clic en el botón
            # escribir un mensaje
    st.write("Creación de un histograma para el precio de los autos")
            
            # crear un histograma
    fig = px.histogram(vehicles_us, x="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para un gráfico de dispersión.

dist_button = st.button('Construir un gráfico de distribución') # crear un botón
        
if dist_button: # al hacer clic en el botón
                # escribir un mensaje
    st.write('Creación de un gráifico de distribución entre el precio y año del modelo')
            
                # crear un un gráfico de distribución
    fig = px.scatter(vehicles_us, x="model_year", y="price")
    fig.update_traces(marker_color='orange')        

# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)