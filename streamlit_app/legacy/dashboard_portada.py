import streamlit as st
from PIL import Image

# Configuración del dashboard
st.set_page_config(page_title="Tierra Adentro Artesanal", layout="wide")

# Cargar logo
try:
    logo = Image.open("logo_tierra_adentro.PNG")
    col_logo = st.columns([2, 1, 2])
    with col_logo[1]:
        st.image(logo, use_container_width=False, width=250)
except FileNotFoundError:
    st.warning("El logo no se encuentra en la ubicación especificada.")

# Título principal
st.title("🌿 Tierra Adentro Artesanal")
st.write(
    """
    Bienvenidos al dashboard integral de Tierra Adentro Artesanal, donde se explora el desempeño y los valores 
    clave del negocio. Este espacio inicial ofrece una visión general del emprendimiento y de lo que 
    representan sus productos.
    """
)

# Sección de imágenes de portada
st.subheader("📸 Visualización del Negocio")

# Imagen de Instagram
try:
    instagram_portada = Image.open("instagram_portada.PNG")
    st.image(instagram_portada, use_container_width=True, caption="Perfil de Instagram \n Promoción de productos y conexión con clientes")
except FileNotFoundError:
    st.warning("La imagen de Instagram no se encuentra.")

# Imagen de Mercado Libre
try:
    ml_portada = Image.open("ml_portada.PNG")
    st.image(ml_portada, use_container_width=True, caption="Tienda en Mercado Libre \n Venta principal de productos artesanales")
except FileNotFoundError:
    st.warning("La imagen de Mercado Libre no se encuentra.")

# Descripción del negocio
st.subheader("🌟 Acerca de Tierra Adentro Artesanal")
st.write(
    """
    **Tierra Adentro Artesanal** es un emprendimiento argentino dedicado a la creación de productos 
    hechos a mano con cuero legítimo, destacándose por:

    - **Productos principales:** Sandalias, carteras y accesorios de cuero.
    - **Compromiso artesanal:** Combinación de técnicas ancestrales con diseños modernos.
    - **Canales de venta:** Comercialización a través de Mercado Libre y promoción activa en redes sociales como Instagram.
    - **Sustentabilidad:** Uso de materiales naturales y enfoque en prácticas responsables.

    Este negocio conecta tradición y modernidad, ofreciendo a sus clientes artículos únicos y de alta calidad.
    """
)

# Descripción del análisis
st.subheader("🔍 ¿Qué encontrarás en este dashboard?")
st.write(
    """
    Este dashboard integra análisis de las principales áreas del negocio:

    - **Ventas:** Evaluación de ingresos, patrones de consumo y tendencias anuales.
    - **Publicaciones:** Desempeño del portafolio de productos, preferencias de los clientes y colores más vendidos.
    - **Clientes:** Distribución geográfica, fidelización y análisis demográfico.
    - **Envíos:** Optimización de la logística y tiempos de entrega.

    Todo esto con el objetivo de proporcionar herramientas para mejorar la toma de decisiones y 
    maximizar el crecimiento del negocio.
    """
)

# Nota final
st.info(
    "Este dashboard está diseñado para reflejar la esencia y el potencial de Tierra Adentro Artesanal, "
    "destacando su valor en el mercado artesanal argentino."
)



