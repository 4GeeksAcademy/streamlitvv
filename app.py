import streamlit as st
import pandas as pd
import pickle

# Carga del vectorizador TF-IDF y el modelo KNN
tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Carga de los datos de películas
data = pd.read_csv('peliculas.csv')  # Asegúrate de que este archivo esté en el mismo directorio o usa la ruta correcta

def get_recommendations(movie):
    st.write(f"Buscando recomendaciones para: {movie}")
    try:
        # Vectorización del título de la película ingresada
        movie_vector = tfidf_vectorizer.transform([movie])
        st.write(f"Vector de la película: {movie_vector}")

        # Obtener recomendaciones usando KNN
        distances, indices = model.kneighbors(movie_vector, n_neighbors=10)
        st.write(f"Índices de recomendaciones: {indices}")
        
        # Obtener títulos de las películas recomendadas
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

# Interfaz de Streamlit
st.title("Recomendador de Películas")
movie_title = st.text_input("Ingrese el título de una película:")
if movie_title:
    render_results(movie_title)
