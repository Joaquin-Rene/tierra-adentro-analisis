import streamlit as st
from PIL import Image

# Configuración general
st.set_page_config(page_title="Análisis de Clientes", layout="wide")

# Cargar logo si existe
try:
    logo = Image.open("logo_tierra_adentro.PNG")
    col_logo = st.columns([2, 1, 2])
    with col_logo[1]:
        st.image(logo, use_container_width=False, width=250)
except:
    pass

# Título principal
st.title("📈 Análisis de Clientes - Tierra Adentro Artesanal")
st.write(
    """
    Este dashboard presenta un panorama detallado de la cartera de clientes, 
    incluyendo su distribución geográfica, comportamiento de compras y 
    datos demográficos aproximados. El objetivo es entender mejor al 
    público y orientar estrategias comerciales efectivas.
    """
)

# Cargar imágenes
distribucion_provincias = Image.open("distribucion_provincias.png")
distribucion_CABA = Image.open("distribucion_CABA.png")
top_10_ciudadesmasventas = Image.open("top_10_ciudadesmasventas.png")
top_barrios_ventas = Image.open("top_barrios_ventas.png")
rango_dni = Image.open("rango_dni.png")
clientes_compras = Image.open("clientes_compras.png")

# --------------------------
# Sección 1: Distribución por Provincias (en solitario, centrada)
# --------------------------
st.subheader("🗺️ Distribución de Clientes por Provincia")

# Columna central para la imagen
col_prov = st.columns([1, 2, 1])
with col_prov[1]:
    st.image(distribucion_provincias, use_container_width=True)

st.write(
    """
    **Análisis:**
    - El mapa de Argentina muestra la **concentración de clientes** en Buenos Aires, 
      Capital Federal y Córdoba, indicando un foco principal en zonas urbanas.
    - Provincias como Santa Fe, Entre Ríos y Río Negro presentan una cantidad moderada 
      de clientes, sugiriendo un potencial para campañas de expansión regional.
    - **Recomendación:** Reforzar acciones en las provincias líderes (p. ej., Buenos Aires, Córdoba) 
      y explorar alianzas o eventos locales en las provincias de mediana penetración para 
      incrementar la notoriedad y el volumen de clientes.
    """
)

# --------------------------
# Sección 2: Distribución de Ventas en CABA (maximizada)
# --------------------------
st.subheader("🏙️ Distribución de Ventas en CABA")

# Ajustamos las columnas a [1, 6, 1] para maximizar la imagen en el centro
col_caba = st.columns([1, 6, 1])
with col_caba[1]:
    st.image(distribucion_CABA, use_container_width=False, width=1000)

st.write(
    """
    **Análisis:**
    - La visualización de CABA evidencia **puntos de alta concentración** de ventas en 
      barrios céntricos y de mayor poder adquisitivo (Recoleta, Palermo).
    - Los círculos más grandes indican los “hot spots” dentro de la ciudad, concentrando 
      la mayor parte de las compras.
    - **Recomendación:** Ajustar las estrategias logísticas y de marketing digital 
      (geolocalización) para optimizar la presencia en estas zonas de alta demanda, 
      mejorando tiempos de entrega y ofreciendo promociones específicas.
    """
)

# --------------------------
# Sección 3: Ciudades y Barrios con Mayor Volumen de Ventas (lado a lado)
# --------------------------
st.subheader("🌆 Top 10 Ciudades con Mayor Volumen de Ventas (Excluyendo CABA) y Barrios con Más Ventas en CABA")

col_ciudades, col_barrios = st.columns([1, 1])
with col_ciudades:
    st.image(top_10_ciudadesmasventas, use_container_width=True)
    st.write(
        """
        **Análisis (Ciudades):**
        - Córdoba, Rosario y Posadas destacan en el interior, confirmando la existencia 
          de polos de consumo fuera de CABA.
        - Otras ciudades (Pilar, Resistencia) también muestran resultados, lo que indica 
          un mercado disperso pero con focos muy activos.
        - **Recomendación:** Diseñar campañas regionales y colaboraciones con comercios 
          locales para reforzar la presencia en estas plazas y fidelizar a los clientes.
        """
    )

with col_barrios:
    st.image(top_barrios_ventas, use_container_width=True)
    st.write(
        """
        **Análisis (Barrios CABA):**
        - Recoleta y Palermo lideran, seguidos de Caballito y Villa Urquiza, 
          confirmando la relevancia de barrios de alta densidad y poder adquisitivo.
        - Belgrano y Chacarita muestran menor volumen pero potencial de crecimiento.
        - **Recomendación:** Llevar a cabo colaboraciones con comercios de barrio, pop-ups 
          o demostraciones de producto en zonas relevantes, reforzando la 
          cercanía con el cliente.
        """
    )

# --------------------------
# Sección 4: Perfil de Clientes (Rango DNI y Clientes con Más Compras)
# --------------------------
st.subheader("👤 Perfil de Clientes")

col_dni, col_compras = st.columns([1, 1])
with col_dni:
    st.image(rango_dni, use_container_width=True)
    st.write(
        """
        **Análisis (Rango DNI):**
        - Se aprecia un amplio rango de edades (aproximación por DNI), con la mayor cantidad 
          de clientes en el espectro 23-63 años, indicando un público adulto.
        - El rango mayor (63-83 años) es reducido, pero podría representar un nicho que 
          valora productos artesanales de alta calidad.
        - **Recomendación:** Desarrollar campañas segmentadas por edad, resaltando atributos 
          clave (comodidad, estilo, durabilidad) y, para el público mayor, destacar 
          la calidad y la producción artesanal.
        """
    )

with col_compras:
    st.image(clientes_compras, use_container_width=True)
    st.write(
        """
        **Análisis (Clientes con Más Compras):**
        - El top 10 de clientes con más compras muestra 2-3 adquisiciones, 
          lo que indica cierta fidelidad y potencial para programas de lealtad.
        - Incluso si la mayoría de los clientes compra esporádicamente, existe un 
          grupo fiel que puede volverse embajador de marca.
        - **Recomendación:** Implementar estrategias de retención (descuentos por lealtad, 
          membresías, early access a lanzamientos) para premiar la recompra 
          y fomentar el boca a boca positivo.
        """
    )

# --------------------------
# Resumen Final
# --------------------------
st.write("---")
st.info(
    """
    **Conclusiones y Recomendaciones Principales:**
    - **Ampliar la Penetración Regional:** El grueso de clientes se concentra en 
      Buenos Aires y zonas puntuales del interior (Córdoba, Rosario, Misiones). 
      Es conveniente desarrollar acciones locales específicas para consolidar 
      la marca fuera de CABA.
    - **Segmentación y Fidelización:** La franja etaria más activa (23-63 años) 
      demanda campañas orientadas a estilo, comodidad y calidad. 
      Además, potenciar planes de lealtad para clientes recurrentes que puedan 
      convertirse en “embajadores” de la marca.
    - **Optimización en CABA:** Reforzar la logística y la presencia en barrios de 
      alta densidad y poder adquisitivo (Recoleta, Palermo). 
      Aprovechar herramientas de marketing digital con geolocalización y 
      colaboraciones locales.

    **Orientación Publicitaria:**
    - **Marketing Geolocalizado:** Enfocar publicidad online (Facebook Ads, Google Ads) 
      en barrios y ciudades detectadas como “hot spots”.
    - **Colaboraciones Locales:** Participar en ferias, acuerdos con tiendas o restaurantes 
      para exhibir o vender productos en las regiones de mayor potencial.
    - **Contenido Personalizado:** Crear mensajes segmentados que resuenen con el rango 
      etario principal, destacando atributos diferenciadores (calidad artesanal, durabilidad, estilo).
    """
)



#streamlit run dashboard_clientes.py