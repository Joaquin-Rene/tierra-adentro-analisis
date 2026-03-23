import streamlit as st
from PIL import Image

# Configuración del dashboard
st.set_page_config(page_title="Análisis de Envíos", layout="wide")

# Cargar logo (opcional)
try:
    logo = Image.open("logo_tierra_adentro.PNG")
    col_logo = st.columns([2, 1, 2])
    with col_logo[1]:
        st.image(logo, use_container_width=False, width=250)
except:
    pass

# Título principal
st.title("🚚 Análisis de Envíos - Tierra Adentro Artesanal")
st.write(
    """
    Este dashboard muestra información clave sobre los tiempos y patrones de envío,
    ayudando a optimizar la logística y mejorar la experiencia del cliente.
    """
)

# Cargar imágenes
tiempo_entrega = Image.open("promedio_entrega.png")
intervalo_tiempo = Image.open("envios_tiempo.png")
envios_dia_semana = Image.open("envios_semana.png")

# --------------------------
# Sección 1: Tiempo Promedio de Entrega
# --------------------------
st.subheader("⏱️ Tiempo Promedio de Entrega")
st.image(tiempo_entrega, use_container_width=True)
st.write(
    """
    **Análisis:**
    - El tiempo promedio de entrega se ubica en **5.09 días**, un valor razonable
      para envíos nacionales, aunque podría optimizarse para destacar frente a la competencia.
    - Conviene monitorear este indicador regularmente para detectar variaciones estacionales
      o problemas específicos (logística, abastecimiento, etc.).

    **Recomendación:**
    - Explorar acuerdos con transportistas o servicios exprés para reducir aún más
      el tiempo de tránsito, especialmente en temporadas de alta demanda.
    - Brindar transparencia al cliente (tracking y notificaciones) para aumentar la
      satisfacción y minimizar reclamos.
    """
)

# --------------------------
# Sección 2: Envíos por Intervalo de Tiempo del Día
# --------------------------
st.subheader("🌗 Envíos por Intervalo de Tiempo del Día")
st.image(intervalo_tiempo, use_container_width=True)
st.write(
    """
    **Análisis:**
    - La mayoría de los envíos se procesan durante la **tarde (201)**, seguida de la noche (25) y la mañana (22).
    - Este patrón podría indicar que gran parte del personal u operación logística 
      se concentra en la segunda mitad del día.
    
    **Recomendación:**
    - Evaluar turnos escalonados para no saturar la jornada vespertina, distribuyendo 
      mejor la carga de trabajo y reduciendo potenciales retrasos.
    - Considerar si hay oportunidades o costos más bajos al despachar más productos 
      en horas nocturnas, aprovechando menos congestión de tráfico o tarifas de envío diferenciales.
    """
)

# --------------------------
# Sección 3: Envíos por Día de la Semana
# --------------------------
st.subheader("📅 Envíos por Día de la Semana")
st.image(envios_dia_semana, use_container_width=True)
st.write(
    """
    **Análisis:**
    - Los picos de envíos aparecen los **Miércoles y Lunes** (50 cada uno), lo cual 
      sugiere una acumulación de pedidos tras el fin de semana y a mitad de semana.
    - El menor volumen se registra los sábados (22), aunque se siguen realizando despachos
      para mantener el flujo de entregas.
    
    **Recomendación:**
    - Fortalecer la dotación de personal o coordinación con transportistas a inicios de semana
      y a mitad de semana, cuando se concentran los despachos.
    - Evaluar la conveniencia de mantener operaciones los sábados para disminuir la 
      acumulación de pedidos el lunes.
    """
)

# --------------------------
# Resumen Final
# --------------------------
st.write("---")
st.info(
    """
    **Conclusiones Generales:**
    - El tiempo de entrega promedio (~5 días) es aceptable, pero hay espacio para la mejora 
      que ofrezca un diferencial competitivo.
    - El **turno tarde** concentra la mayor parte de la actividad de despacho, 
      pudiendo generar cuellos de botella si el volumen de pedidos aumenta.
    - Los **miércoles y lunes** sobresalen como días pico de envíos, necesitando más recursos 
      y coordinación con transportistas.

    **Líneas de Acción Sugeridas:**
    1. **Optimizar la Cadena Logística:** Considerar transportistas alternativos y/o 
       servicios exprés para disminuir el tiempo de tránsito.
    2. **Distribución de Turnos:** Equilibrar la carga de trabajo entre la tarde y el resto 
       del día, evitando saturaciones y retrasos.
    3. **Planificación de Días Pico:** Refuerzo de personal y recursos lunes/miércoles para 
       manejar el pico de despachos.
    4. **Comunicación Proactiva:** Ofrecer seguimiento de pedidos y tiempos estimados a 
       los clientes, fomentando confianza y transparencia.
    """
)

#streamlit run dashboard_envios.py