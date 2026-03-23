import streamlit as st
from PIL import Image

# Configuración del dashboard
st.set_page_config(page_title="Análisis de Productos", layout="wide")

# Cargar logo (opcional, si lo tienes)
try:
    logo = Image.open("logo_tierra_adentro.PNG")
    # Encabezado con logo centrado
    col_logo = st.columns([2, 1, 2])
    with col_logo[1]: 
        st.image(logo, use_container_width=False, width=250)
except:
    pass

# Título principal
st.title("📦 Análisis de Productos - Tierra Adentro Artesanal")
st.write("Evaluación detallada del portafolio de productos, considerando su tipo, volumen de ventas, ingresos y preferencias de color.")

# Cargar imágenes
sandalias_vendidas = Image.open("sandalias_vendidas.png")
conteo_tipo_producto = Image.open("conteo_tipo_producto.png")
ingresos_productos = Image.open("ingresos_productos.png")
distribucion_colores_productos = Image.open("distribucion_colores_productos.png")
ingresos_colores_productos = Image.open("ingresos_colores_productos.png")
top_10_productos_vendidos = Image.open("top_10_productos_vendidos.png")
top_10_sincalzados = Image.open("top_10_sincalzados.png")
top_10_masingresos = Image.open("top_10_masingresos.png")


# --------------------------
# Sección 1: Visión General de Tipos de Productos
# --------------------------
st.subheader("🗂 Distribución por Tipo de Producto")
col_a, col_b = st.columns([2, 2])

with col_a:
    st.image(conteo_tipo_producto, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - El conteo de publicaciones por tipo de producto muestra que las **Sandalias** son, por amplio margen, el tipo más frecuente en el portafolio.
        - Otros tipos (Estuches, Fundas, Alpargatas, Pantuflas, etc.) presentan menor variedad, indicando una cartera centrada en calzado.
        - **Recomendación:** Explorar la diversificación en tipos de productos con mayor demanda potencial o agregar valor a los ya existentes (como estuches o fundas), ajustando estrategias de marketing que destaquen su utilidad y calidad.
        """
    )

with col_b:
    st.image(ingresos_productos, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - Los ingresos totales por tipo de producto evidencian que la categoría **Sandalia** lidera ampliamente en términos de facturación, reflejando su alta demanda e importancia estratégica.
        - Otros productos contribuyen a diversificar el riesgo, pero su impacto en ingresos es relativamente menor.
        - **Recomendación:** Potenciar aún más la categoría líder (Sandalias) con modelos diferenciados y mayor exposición de marca, a la vez que se busca elevar la rentabilidad y reconocimiento de otros tipos de productos mediante campañas y alianzas estratégicas.
        """
    )

# --------------------------
# Sección 2: Profundizando en Sandalias y otros Productos
# --------------------------
st.subheader("👠 Análisis de Sandalias y Productos Destacados")

col_c, col_d = st.columns([2, 2])
with col_c:
    st.image(sandalias_vendidas, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - Entre las sandalias más vendidas (Top 10), se evidencia una preferencia por modelos de cuero auténtico y diseños atemporales.
        - El liderazgo en ingresos de ciertas sandalias (como "Sandalias Cuero Atenea") indica que el cliente valora calidad y diseño distintivo.
        - **Recomendación:** Mantener el catálogo de modelos exitosos, y en paralelo, lanzar ediciones limitadas o colecciones cápsula que incentiven compras recurrentes y fidelización.
        """
    )

with col_d:
    st.image(top_10_productos_vendidos, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - El Top 10 de productos más vendidos (en cantidad) exhibe el dominio de las sandalias, pero también la aparición de calzados alternativos y algunos accesorios.
        - Esto sugiere que, si bien el core del negocio sigue siendo el calzado, existen nichos interesados en otros productos.
        - **Recomendación:** Aprovechar los productos ya posicionados como éxitos de venta para atraer clientes hacia categorías emergentes, por ejemplo, empaquetando productos complementarios (alpargatas + estuche, sandalia + cartera).
        """
    )

# --------------------------
# Sección 3: Productos no Calzados y Análisis por Ingresos
# --------------------------
st.subheader("👜 Productos Sin Calzado y Líderes en Ingresos")

col_e, col_f = st.columns([2, 2])
with col_e:
    st.image(top_10_sincalzados, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - El Top 10 sin calzado muestra que las Fundas, Estuches y Portfolios también generan interés, aunque con menor volumen que el calzado.
        - Estos productos no calzados pueden agregar valor percibido a la marca al diversificar la oferta y atraer segmentos específicos (ejecutivos, viajeros, amantes de la papelería artesanal).
        - **Recomendación:** Comunicar claramente la calidad artesanal y el origen de la materia prima (cuero genuino) para posicionar estos accesorios como complementos indispensables para el consumidor actual.
        """
    )

with col_f:
    st.image(top_10_masingresos, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - El Top 10 por ingresos totales incluye tanto sandalias como accesorios premium (ej. Desk Pad Cuero XXL), lo que refleja que ciertos productos no calzados pueden ser altamente rentables.
        - Esto sugiere la existencia de nichos dispuestos a pagar más por artículos de mayor valor agregado y calidad premium.
        - **Recomendación:** Invertir en marketing dirigido a clientes corporativos, hoteles boutique o tiendas especializadas, ofreciendo productos premium con mayor margen. 
        """ 
    )

# --------------------------
# Sección 4: Análisis de Colores
# --------------------------
st.subheader("🎨 Preferencias de Color en el Portafolio")

col_g, col_h = st.columns([2, 2])
with col_g:
    st.image(distribucion_colores_productos, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - La distribución de colores revela una preferencia marcada por tonalidades de marrón, negro y marrón oscuro, alineadas con la estética rústica y artesanal de la marca.
        - Los colores más claros o llamativos (como azul, rojo) son menos frecuentes, reflejando quizás una demanda más conservadora o una oferta limitada.
        - **Recomendación:** Mantener un inventario robusto en los colores más vendidos (marrones, negros), pero considerar ediciones limitadas en colores especiales para testear la respuesta del mercado y ampliar la paleta cuando sea rentable.
        """
    )

with col_h:
    st.image(ingresos_colores_productos, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - En términos de ingresos, los colores terrosos y negro generan la mayor facturación, lo que valida la preferencia del cliente hacia la gama cromática tradicional.
        - Colores menos comunes aportan menos ingresos, indicando que no son el foco principal del público actual.
        - **Recomendación:** Alinear las decisiones de producción con la demanda, priorizando materia prima y recursos para las tonalidades más rentables. Opcionalmente, lanzar ediciones en colores distintos como estrategia de marketing estacional.
        """
    )

# --------------------------
# Resumen Final
# --------------------------
st.write("---")
st.info(
    """
    **Resumen Final:**
    - **Enfoque en Calzado (Sandalias):** El portafolio actual está fuertemente orientado a las sandalias, que dominan tanto en cantidad de publicaciones como en ingresos. Este liderazgo debe mantenerse con innovación de diseños y comunicación efectiva.
    - **Diversificación Controlada:** Aunque las sandalias generan la mayoría de los ingresos, existen otros tipos de productos y accesorios con potencial. Es crucial seguir testeando el mercado, comunicando el valor artesanal y maximizando la rentabilidad de estos nichos.
    - **Colores Clave:** La paleta cromática centrada en marrones y negro es la más exitosa. Mantener el foco en estas tonalidades garantiza optimizar inventario y atraer al público fiel a la estética tradicional.
    - **Premium y Diferenciación:** Algunos productos premium (como desk pads y fundas de cuero) alcanzan ingresos importantes. Potenciar esta línea y orientarla a segmentos dispuestos a pagar un precio superior puede mejorar la rentabilidad general.
    
    En conjunto, este análisis ofrece una hoja de ruta para consolidar el éxito de las sandalias, diversificar estratégicamente, optimizar la oferta de colores y capitalizar en productos premium, permitiendo a Tierra Adentro Artesanal fortalecer su posicionamiento y adaptarse a las preferencias cambiantes del mercado.
    """
)
#streamlit run dashboard_publicaciones.py