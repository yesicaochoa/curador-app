import streamlit as st
import openai
import json

st.title("🎨 Curador Personal de Arte IA")

# Cargar base de datos de artistas
with open("artistas.json", "r", encoding="utf-8") as f:
    artistas = json.load(f)

# Tu clave API OpenAI (la configuras en Streamlit Cloud o la pones acá para probar local)
openai.api_key = st.secrets["OPENAI_API_KEY"]  # o poné tu clave directamente (no recomendado)

def construir_prompt(consulta, artistas):
    artistas_texto = ""
    for a in artistas:
        artistas_texto += f"{a['nombre']}: estilos {', '.join(a['estilo'])}, colores {', '.join(a['colores'])}. Similares: {', '.join(a['similares'])}.\n"
    prompt = f"""
Eres un curador de arte experto. Aquí tienes información de artistas:

{artistas_texto}

Usuario pregunta: {consulta}

Contesta recomendando artistas o estilos relacionados de forma clara y amigable.
"""
    return prompt

consulta_usuario = st.text_input("¿Sobre qué artista o estilo querés preguntar?")

if consulta_usuario:
    prompt = construir_prompt(consulta_usuario, artistas)
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    texto_respuesta = respuesta.choices[0].text.strip()
    st.write(texto_respuesta)
