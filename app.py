import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') 

st.header("Dashboard de Análisis de Vehículos Usados")

hist_button = st.button('Construir histograma') 

if st.checkbox("Visualizar muestra de datos"):
    st.write(car_data.head())
        
if hist_button: 
    st.write(car_data.head())
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.button('Construir grafico de dispersión') 
        
if hist_button_2: 
    st.write(car_data.head())
    fig = px.scatter(car_data, x="odometer", y="price", title= "Precio del vehículo en relación a los KM recorridos y año" ) # crear un gráfico de dispersión
    fig.show()