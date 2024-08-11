import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo y el dataset
model = pickle.load(open('model.pkl', 'rb'))
data = pd.read_csv('C:\\Users\\Fukushima\\Documents\\GitHub\\streamlitvv\\peliculas.csv')

def get_recommendations(movie):
    st.write(f"Buscando recomendaciones para: {movie}")
    # Aquí se asume que `model` es tu modelo entrenado y `data` es tu DataFrame
    try:
        # Supongamos que estás utilizando un sistema de recomendación basado en similitud
        movie_index = data[data['title'].str.contains(movie, case=False)].index[0]
        st.write(f"Índice de la película: {movie_index}")
        # Simulando la obtención de recomendaciones
        distances, indices = model.kneighbors(data.iloc[movie_index, :].values.reshape(1, -1), n_neighbors=10)
        st.write(f"Índices de recomendaciones: {indices}")
        recommendations = data['title'].iloc[indices[0]].tolist()
        return recommendations
    except Exception as e:
        st.write(f"Error al obtener recomendaciones: {e}")
        return []

def render_results(movie):
    recommendations = get_recommendations(movie)
    if recommendations:
        st.write("Películas recomendadas:")
        for rec in recommendations:
            st.write(f"- {rec}")
    else:
        st.write("No se encontraron recomendaciones.")
