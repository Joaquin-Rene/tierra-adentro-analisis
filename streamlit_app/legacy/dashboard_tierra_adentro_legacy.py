import streamlit as st
from PIL import Image

# ------------------------------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Tierra Adentro Artesanal - Dashboard Integral",
    layout="wide"
)

# ------------------------------------------------------------------------------
# LOGO (opcional)
# ------------------------------------------------------------------------------
try:
    logo = Image.open("logo_tierra_adentro.PNG")
    col_logo = st.columns([2, 1, 2])
    with col_logo[1]:
        st.image(logo, use_container_width=False, width=250)
except FileNotFoundError:
    st.warning("No se encontró el archivo de logo (logo_tierra_adentro.PNG).")

# ------------------------------------------------------------------------------
# TÍTULO PRINCIPAL
# ------------------------------------------------------------------------------
st.title("Tierra Adentro Artesanal - Dashboard Integral")

st.markdown(
    """
    Este *single-page app* reúne toda la información de **Portada**, **Ventas**, 
    **Publicaciones (Productos)**, **Clientes**, **Envíos** y **Propuesta de Mejoras** 
    en un solo lugar, permitiendo navegar fácilmente entre las secciones.
    """
)

# ------------------------------------------------------------------------------
# SECCIÓN DE DATOS Y METODOLOGÍA
# ------------------------------------------------------------------------------
with st.expander("📖 Datos y Metodología"):
    st.write(
        """
        **Fuente de datos:**  
        - Exportaciones de Mercado Libre (archivo Excel) con los últimos 6 meses de información 
          de ventas, productos, clientes y envíos.  
        - Para el análisis histórico (2021-2024), se combinan registros previos 
          con proyecciones hasta Octubre 2024.

        **Alcance temporal:**  
        - Ventas: desde 2021 hasta octubre 2024 para la parte histórica.  
        - Publicaciones: catálogo principal vigente (sandalias, accesorios, etc.).  
        - Clientes: distribución geográfica y comportamiento de compras (últimos 6 meses).  
        - Envíos: tiempos de entrega, días y turnos predominantes (últimos 6 meses).

        **Cálculo de indicadores:**  
        - *Ingresos*, *Ventas mensuales*, *Tiempo promedio de entrega*, etc., 
          se basan en agregaciones simples (promedios, sumas) y proyecciones nominales.  
        - El *rango de DNI* se asume como estimador de la edad, sin otros datos personales.

        **Objetivo:**  
        - Brindar una visión integral del desempeño del negocio, 
          orientando la toma de decisiones en marketing, logística, 
          diversificación de productos y estrategias de crecimiento.
        """
    )

# ------------------------------------------------------------------------------
# CREACIÓN DE PESTAÑAS
# ------------------------------------------------------------------------------
tab_portada, tab_ventas, tab_publicaciones, tab_clientes, tab_envios, tab_mejoras = st.tabs(
    ["Portada", "Ventas", "Publicaciones", "Clientes", "Envíos", "Propuesta de Mejoras"]
)

# ==============================================================================
# TAB 1: PORTADA
# ==============================================================================
with tab_portada:
    st.subheader("🌿 Portada - Tierra Adentro Artesanal")

    st.write(
        """
        Bienvenidos al **dashboard integral** de Tierra Adentro Artesanal, 
        donde se explora el desempeño y los valores clave del negocio. 
        Este espacio inicial ofrece una visión general del emprendimiento 
        y de lo que representan sus productos.
        """
    )

    st.subheader("📸 Visualización del Negocio")
    # Imagen de Instagram
    try:
        instagram_portada = Image.open("instagram_portada.PNG")
        st.image(
            instagram_portada,
            use_container_width=True,
            caption="Perfil de Instagram\nPromoción de productos y conexión con clientes"
        )
    except FileNotFoundError:
        st.warning("No se encontró la imagen instagram_portada.PNG.")

    # Imagen de Mercado Libre
    try:
        ml_portada = Image.open("ml_portada.PNG")
        st.image(
            ml_portada,
            use_container_width=True,
            caption="Tienda en Mercado Libre\nVenta principal de productos artesanales"
        )
    except FileNotFoundError:
        st.warning("No se encontró la imagen ml_portada.PNG.")

    st.subheader("🌟 Acerca de Tierra Adentro Artesanal")
    st.write(
        """
        **Tierra Adentro Artesanal** es un emprendimiento argentino dedicado a la creación de productos 
        hechos a mano con cuero legítimo, destacándose por:

        - **Productos principales:** Sandalias, carteras y accesorios de cuero.
        - **Compromiso artesanal:** Combina técnicas ancestrales con diseños modernos.
        - **Canales de venta:** Comercialización vía Mercado Libre y promoción en redes (Instagram).
        - **Sustentabilidad:** Uso de materiales naturales y enfoque en prácticas responsables.

        El negocio conecta tradición y modernidad, ofreciendo a los clientes artículos 
        únicos y de alta calidad.
        """
    )

    st.subheader("🔍 ¿Qué encontrarás en este dashboard?")
    st.write(
        """
        - **Ventas:** Evaluación de ingresos, patrones de consumo y tendencias anuales.
        - **Publicaciones:** Desempeño del portafolio de productos, preferencias de los clientes y colores más vendidos.
        - **Clientes:** Distribución geográfica, fidelización y análisis demográfico.
        - **Envíos:** Optimización de la logística y tiempos de entrega.
        - **Propuesta de Mejoras:** Acciones concretas para impulsar la rentabilidad y el crecimiento a partir de estos hallazgos.
        """
    )

    st.info(
        "Este dashboard está diseñado para reflejar la esencia y el potencial de Tierra Adentro Artesanal, "
        "destacando su valor en el mercado artesanal argentino."
    )

# ==============================================================================
# TAB 2: VENTAS
# ==============================================================================
with tab_ventas:
    st.subheader("📊 Resumen Anual de Ventas - Tierra Adentro Artesanal")
    st.write("Análisis del desempeño de ventas, ingresos y tendencias anuales hasta Octubre 2024.")

    # Ejemplo de imágenes (ajusta nombres según tus archivos)
    try:
        cantidad_ventas_anual = Image.open("cantidad_ventas_anual.png")
        ingresos_bruto = Image.open("ingresos_bruto.png")
        ingresos_totales = Image.open("ingresos_totales.png")
        cargo_impuesto = Image.open("cargo_impuesto.png")
    except FileNotFoundError:
        st.warning("Alguna de las imágenes de Ventas no se encontró.")

    # Visualización 1 y 2
    col1, col2 = st.columns([2, 2])
    with col1:
        st.subheader("📈 Cantidad de Ventas Anual")
        try:
            st.image(cantidad_ventas_anual, use_container_width=True)
        except:
            pass
        st.write("""
        **Análisis:**
        - Caída progresiva de ventas (2021=504 vs 2024=254), ligada a la pérdida de poder adquisitivo.
        - Se proyecta leve recuperación en 2024, aunque no asegurada.
        """)

    with col2:
        st.subheader("💰 Ingresos Brutos Totales por Año")
        try:
            st.image(ingresos_bruto, use_container_width=True)
        except:
            pass
        st.write("""
        **Análisis:**
        - Incremento nominal impulsado por inflación y ajustes de precios.
        - Refleja más la devaluación monetaria que un crecimiento real en la demanda.
        """)

    st.subheader("🧾 Ingresos Totales por Año")
    try:
        st.image(ingresos_totales, use_container_width=True)
    except:
        pass
    st.write("""
    **Análisis:**
    - Pasan de $1.5M en 2021 a $5.7M en 2024, principalmente por inflación.
    - Es clave enfocarse en la rentabilidad real tras descontar costos e impuestos.
    """)

    st.subheader("📉 Cargo de Impuesto Mensual")
    try:
        st.image(cargo_impuesto, use_container_width=True)
    except:
        pass
    st.write("""
    **Análisis:**
    - Alto impacto sobre los márgenes.
    - Supera $500K en Septiembre, reflejando presión fiscal.
    """)

    # Nuevas visualizaciones
    st.subheader("📅 Ventas por Mes (2024)")
    try:
        ventas_mes = Image.open("ventas_mes.png")
        st.image(ventas_mes, use_container_width=True)
    except:
        pass

    st.subheader("📆 Ventas por Día de la Semana (2024)")
    try:
        ventas_semana = Image.open("ventas_semanas.png")
        st.image(ventas_semana, use_container_width=True)
    except:
        pass

    st.subheader("⏰ Horas Pico de Venta (2024)")
    try:
        hora_pico_ventas = Image.open("hora_pico_ventas.png")
        st.image(hora_pico_ventas, use_container_width=True)
    except:
        pass

    st.write("---")
    st.info("""
    **Resumen (Ventas):**
    - Inflación eleva ingresos nominales, mientras disminuyen las unidades vendidas.
    - Carga impositiva fuerte, requiere estrategias para optimizar costos e impuestos.
    - Se observan picos estacionales, semanales y por horario, valiosos para ajustar marketing y inventario.
    """)


# ==============================================================================
# TAB 3: PUBLICACIONES (Productos)
# ==============================================================================
with tab_publicaciones:
    st.subheader("📦 Análisis de Productos - Tierra Adentro Artesanal")
    st.write("Evaluación detallada del portafolio de productos, considerando su tipo, volumen de ventas, ingresos y preferencias de color.")

    # Cargar imágenes si existen
    try:
        sandalias_vendidas = Image.open("sandalias_vendidas.png")
        conteo_tipo_producto = Image.open("conteo_tipo_producto.png")
        ingresos_productos = Image.open("ingresos_productos.png")
        distribucion_colores_productos = Image.open("distribucion_colores_productos.png")
        ingresos_colores_productos = Image.open("ingresos_colores_productos.png")
        top_10_productos_vendidos = Image.open("top_10_productos_vendidos.png")
        top_10_sincalzados = Image.open("top_10_sincalzados.png")
        top_10_masingresos = Image.open("top_10_masingresos.png")
    except FileNotFoundError:
        st.warning("Alguna imagen de Publicaciones no se encontró.")

    # Sección 1: Visión General de Tipos de Productos
    st.subheader("🗂 Distribución por Tipo de Producto")
    col_a, col_b = st.columns([2, 2])
    with col_a:
        try:
            st.image(conteo_tipo_producto, use_container_width=True)
        except:
            pass
        st.write("""
        **Análisis:**
        - Sandalias lideran el portafolio, otros tipos (Estuches, Fundas, etc.) menores en cantidad.
        - **Recomendación:** Diversificar aprovechando potencial de categorías de accesorios.
        """)
    with col_b:
        try:
            st.image(ingresos_productos, use_container_width=True)
        except:
            pass
        st.write("""
        **Análisis:**
        - Ingresos dominados por sandalias, otros productos diversifican riesgo pero con menor impacto.
        - **Recomendación:** Mantener la categoría líder y reforzar branding de accesorios con alto valor agregado.
        """)

    st.subheader("👠 Análisis de Sandalias y Productos Destacados")
    col_c, col_d = st.columns([2, 2])
    with col_c:
        try:
            st.image(sandalias_vendidas, use_container_width=True)
        except:
            pass
        st.write("""
        **Sandalias más vendidas:** Preferencia por cuero auténtico y diseño atemporal.
        """)
    with col_d:
        try:
            st.image(top_10_productos_vendidos, use_container_width=True)
        except:
            pass
        st.write("""
        **Top 10 en cantidad:** Sandalias dominan, accesorios emergen como alternativa.
        """)

    st.subheader("👜 Productos Sin Calzado y Líderes en Ingresos")
    col_e, col_f = st.columns([2, 2])
    with col_e:
        try:
            st.image(top_10_sincalzados, use_container_width=True)
        except:
            pass
        st.write("""
        **Análisis:** Fundas, Estuches y Portfolios añaden valor percibido al catálogo.
        """)
    with col_f:
        try:
            st.image(top_10_masingresos, use_container_width=True)
        except:
            pass
        st.write("""
        **Análisis:** Accesorios premium generan ingresos altos en nichos específicos (ej. Desk Pad).
        """)

    st.subheader("🎨 Preferencias de Color en el Portafolio")
    col_g, col_h = st.columns([2, 2])
    with col_g:
        try:
            st.image(distribucion_colores_productos, use_container_width=True)
        except:
            pass
        st.write("""
        **Distribución de colores:** Marrón y negro predominan.
        """)
    with col_h:
        try:
            st.image(ingresos_colores_productos, use_container_width=True)
        except:
            pass
        st.write("""
        **Ingresos por color:** Tonalidades oscuras lideran en facturación.
        """)

    st.write("---")
    st.info("""
    **Resumen (Publicaciones):**
    - Sandalias = núcleo del portafolio, pero accesorios premium son rentables.
    - Colores terrosos y negro generan la mayor facturación, hay potencial en ediciones limitadas.
    """)


# ==============================================================================
# TAB 4: CLIENTES
# ==============================================================================
with tab_clientes:
    st.subheader("📈 Análisis de Clientes - Tierra Adentro Artesanal")

    try:
        distribucion_provincias = Image.open("distribucion_provincias.png")
        distribucion_CABA = Image.open("distribucion_CABA.png")
        top_10_ciudadesmasventas = Image.open("top_10_ciudadesmasventas.png")
        top_barrios_ventas = Image.open("top_barrios_ventas.png")
        rango_dni = Image.open("rango_dni.png")
        clientes_compras = Image.open("clientes_compras.png")
    except FileNotFoundError:
        st.warning("Alguna imagen de Clientes no se encontró.")

    st.subheader("🗺️ Distribución de Clientes por Provincia")
    col_prov = st.columns([1, 2, 1])
    with col_prov[1]:
        try:
            st.image(distribucion_provincias, use_container_width=True)
        except:
            pass
    st.write("""
    **Análisis:** Foco en BsAs, CABA y Córdoba, con potencial de expansión en otras provincias.
    """)

    st.subheader("🏙️ Distribución de Ventas en CABA")
    col_caba = st.columns([1, 6, 1])
    with col_caba[1]:
        try:
            st.image(distribucion_CABA, use_container_width=False, width=1000)
        except:
            pass
    st.write("""
    **Análisis:** Concentración en barrios de alto poder adquisitivo (Recoleta, Palermo).
    """)

    st.subheader("🌆 Top 10 Ciudades y Barrios")
    col_ciudades, col_barrios = st.columns([1, 1])
    with col_ciudades:
        try:
            st.image(top_10_ciudadesmasventas, use_container_width=True)
        except:
            pass
    with col_barrios:
        try:
            st.image(top_barrios_ventas, use_container_width=True)
        except:
            pass

    st.subheader("👤 Perfil de Clientes")
    col_dni, col_compras = st.columns([1, 1])
    with col_dni:
        try:
            st.image(rango_dni, use_container_width=True)
        except:
            pass
    with col_compras:
        try:
            st.image(clientes_compras, use_container_width=True)
        except:
            pass

    st.write("---")
    st.info("""
    **Resumen (Clientes):**
    - Mayoría en BsAs/CABA, con edades 23-63.
    - Fidelización y expansión regional son claves para el crecimiento.
    """)


# ==============================================================================
# TAB 5: ENVÍOS
# ==============================================================================
with tab_envios:
    st.subheader("🚚 Análisis de Envíos - Tierra Adentro Artesanal")

    try:
        tiempo_entrega = Image.open("promedio_entrega.png")
        intervalo_tiempo = Image.open("envios_tiempo.png")
        envios_dia_semana = Image.open("envios_semana.png")
    except FileNotFoundError:
        st.warning("Alguna imagen de Envíos no se encontró.")

    st.subheader("⏱️ Tiempo Promedio de Entrega")
    try:
        st.image(tiempo_entrega, use_container_width=True)
    except:
        pass
    st.write("""
    **Análisis:** ~5 días de entrega, aceptable pero mejorable.
    """)

    st.subheader("🌗 Envíos por Intervalo de Tiempo del Día")
    try:
        st.image(intervalo_tiempo, use_container_width=True)
    except:
        pass
    st.write("""
    **Análisis:** Concentración en turno tarde (201 envíos).
    """)

    st.subheader("📅 Envíos por Día de la Semana")
    try:
        st.image(envios_dia_semana, use_container_width=True)
    except:
        pass
    st.write("""
    **Análisis:** Picos lunes/miércoles (50), menor volumen sábados.
    """)

    st.write("---")
    st.info("""
    **Resumen (Envíos):**
    - Tiempo de entrega ~5 días, saturación en la tarde, picos lunes/miércoles.
    - Ajustar personal y turnos, explorar opciones exprés.
    """)


# ==============================================================================
# TAB 6: PROPUESTA DE MEJORAS
# ==============================================================================
with tab_mejoras:
    st.subheader("💡 Propuesta de Mejoras - Rentabilidad y Próximos Pasos")

    st.markdown("""
    A partir de todos los hallazgos en **Ventas, Publicaciones, Clientes y Envíos**, 
    surgen estas propuestas para **impulsar la rentabilidad** y 
    **fortalecer la presencia digital**:
    """)

    st.write("### 1. Acciones Inmediatas")
    st.markdown("""
    - **Ajuste de Costos y Estrategia de Precios:**  
      Reforzar la negociación con proveedores de cuero, revisar 
      costos fijos y variables para mantener márgenes reales en un entorno inflacionario.  
      Ajustar precios con subas escalonadas, previendo la reacción del mercado.

    - **Campañas Publicitarias en Instagram:**  
      - **Contenido de Valor**: Mostrar el proceso artesanal (videos de manufactura, historias) 
        para conectar con el público.  
      - **Uso de Reels y Historias Destacadas**: Mayor alcance y engagement orgánico.  
      - **Colaboraciones con Influencers**: Segmentar por estilo de vida (turismo, moda sustentable, etc.) 
        para llegar a clientes afines.

    - **Promociones y Cupones Cruzados:**  
      Ofrecer descuentos específicos para quienes compren productos complementarios 
      (ej. Sandalias + Estuche, Desk Pad + Cartera). Esto eleva el ticket promedio y 
      fomenta venta cruzada.

    - **Optimizar Envíos**:  
      - Reforzar la dotación de personal lunes y miércoles, 
        evitando cuellos de botella en el turno tarde.  
      - Evaluar servicios de mensajería exprés en zonas de alta demanda (Recoleta, Palermo) 
        para reducir a 2-3 días el plazo.

    - **Gestión Fiscal Inteligente:**  
      Asesorarse para el uso de regímenes especiales o exenciones 
      (ej. monotributo social, PyME) en caso de corresponder, reduciendo la carga impositiva.
    """)

    st.write("### 2. Impulsar más las Ventas por Instagram")
    st.markdown("""
    - **Catálogo Interactivo**: Aprovechar la funcionalidad de "Shop" en Instagram para etiquetar productos.  
    - **Historias con Enlace Directo**: Si se dispone de más de 10k seguidores o cuenta comercial verificada, 
      incluir links directos a Mercado Libre o a una tienda online propia.  
    - **Publicidad Segmentada** (Facebook Ads / Instagram Ads):  
      - Enfocar en públicos de alto poder adquisitivo, 
        geolocalizados en zonas donde hay potencial de crecimiento (ej. ciudades con ventas moderadas pero emergentes).
    """)

    st.write("### 3. Cómo Seguir y Qué Más Analizar")
    st.markdown("""
    - **Datos de Redes Sociales**:  
      - Extraer métricas de Instagram Insights (alcance, impresiones, engagement) 
        y correlacionarlas con picos de ventas para optimizar lanzamientos.  
      - Analizar la tasa de conversión de las visitas a la página de Instagram hacia Mercado Libre.

    - **Información de Mercado Libre**:  
      - Revisar reseñas y calificaciones para detectar oportunidades de mejora en productos o envíos.  
      - Hacer un seguimiento de carritos abandonados (si la plataforma lo permite) para entender 
        en qué punto se pierde al cliente.

    - **Automatización de Reportes**:  
      - Programar la extracción de datos mensualmente y alimentar un dashboard dinámico 
        (Podrías, por ejemplo, integrar con Google Sheets o una base de datos local).  
      - Incluir análisis de “lifetime value” (LTV) de clientes y retención a largo plazo, 
        si se dispone de históricos suficientes.

    - **Segmentación Avanzada**:  
      - Enriquecer el perfil del cliente con encuestas, preferiblemente dentro de la experiencia 
        post-compra, para identificar motivaciones y sugerir productos afines.  
      - Categorizar clientes según frecuencia de compra, ticket promedio y preferencias de producto.

    - **Planes de Referidos**:  
      - Incentivar a clientes satisfechos a recomendar la marca a familiares y amigos.  
      - Ofrecer descuentos o regalos simbólicos como cupones (ej. “Invita a un amigo y ambos obtienen 10% off”).

    Con estas líneas de acción, **Tierra Adentro Artesanal** puede continuar escalando sus ventas, 
    preservar la rentabilidad real, fortalecer su marca en Instagram y lograr mayor fidelización 
    de clientes gracias a un entendimiento más profundo de sus necesidades.
    """)

    st.success("""
    **Conclusión:**  
    La clave es mantener la **calidad artesanal** e identidad de la marca, 
    al tiempo que se implementan mejoras operativas y estrategias de marketing 
    segmentadas. Con un seguimiento continuo y mayor integración de datos, 
    se podrá tomar decisiones más ágiles y eficaces para crecer en un mercado desafiante.
    """)

# ==============================================================================
# Conclusiones Globales (Opcional)
# ==============================================================================
st.write("---")
with st.expander("📌 Conclusiones Globales (Revisión Rápida)"):
    st.markdown(
        """
        - **Ventas:** Ingresos nominales suben, unidades vendidas bajan. Inflación y 
          carga impositiva altos. Importante afinar estrategias de precios y costos.
        - **Publicaciones (Productos):** Sandalias dominan, accesorios premium rentables, 
          colores oscuros preferidos. Alianzas y colecciones limitadas son clave.
        - **Clientes:** Concentración en CABA y Buenos Aires, rango etario 23-63, 
          planes de fidelización y expansión regional.
        - **Envíos:** 5 días promedio, pico lunes/miércoles y turno tarde, 
          se sugiere escalonar logística y evaluar envíos exprés.

        **¡Consulta la pestaña “Propuesta de Mejoras”** para ver acciones 
        concretas a implementar y sugerencias de análisis futuro.
        """
    )




#streamlit run dashboard_tierra_adentro.py
