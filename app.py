import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') 
hist_button = st.button('Construir histograma') 
        
if hist_button: 
    st.write("vehicles_us.csv")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.button('Construir grafico de dispersión') 
        
if hist_button_2: 
    st.write("vehicles_us.csv")
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    fig.show()