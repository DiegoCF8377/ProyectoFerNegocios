import streamlit as st
st.image("Principa.png")

# Título con estilo
st.title("Capa de Ozono")

# Texto con formato
st.write("Aquí encontrarás Lo ultimo en moda")

# Imágenes con títulos y dimensiones personalizadas
st.image("captura.png", caption="Últimos videos populares en TikTok", width=300)
st.image("Payaso.png", caption="Zapatos elegantes :D", width=300)
st.markdown(
    """
    <audio autoplay controls>
      <source src="Balenciaga meme song  Thip Trong  Lightvessel.mp3" type="audio/mpeg">
      Tu navegador no soporta la reproducción de audio.
    </audio>
    """,
    unsafe_allow_html=True,
)