import streamlit as st
import json

st.title("🎨 Curador Personal de Arte")

# Cargar la base de datos
with open("artistas.json", "r", encoding="utf-8") as f:
    artistas = json.load(f)

# Entrada del usuario
nombre_usuario = st.text_input("¿Qué artista o estilo te gusta?")

# Buscar coincidencia en la base
def buscar_artista(nombre):
    nombre = nombre.lower()
    for artista in artistas:
        if nombre in artista["nombre"].lower():
            return artista
    return None

# Mostrar resultado
if nombre_usuario:
    resultado = buscar_artista(nombre_usuario)
    if resultado:
        st.subheader(f"🧠 Si te gusta {resultado['nombre']}, podrías explorar:")
        for similar in resultado["similares"]:
            st.write(f"• {similar}")
        st.markdown(f"**Estilos:** {', '.join(resultado['estilo'])}")
        st.markdown(f"**Colores frecuentes:** {', '.join(resultado['colores'])}")
    else:
        st.warning("No encontré ese artista. Probá con otro nombre o estilo.")
