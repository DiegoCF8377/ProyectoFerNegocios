import streamlit as st
st.image("Principa.png",use_column_width=True)

# Título con estilo
st.title("Pisa fuerte, marca tendencia con Capa de Ozono")
st.video("video.mp4", format="video/mp4", start_time=0)
# Texto con formato
st.subheader("""Aquí encontrarás Lo ultimo en moda""")

# Imágenes con títulos y dimensiones personalizadas
st.image("captura.png", caption="Últimos videos populares en TikTok", width=300)
st.image("Payaso.png", caption="Zapatos elegantes :D", width=300)
