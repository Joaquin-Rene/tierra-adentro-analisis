import streamlit as st
from PIL import Image

# Configuración del dashboard
st.set_page_config(page_title="Resumen Anual de Ventas", layout="wide")

# Cargar logo
logo = Image.open("logo_tierra_adentro.PNG")  # Asegúrate que el archivo esté en la misma carpeta

# Encabezado con logo centrado
col_logo = st.columns([2, 1, 2])  # Dividir en columnas para centrar el logo
with col_logo[1]: 
    st.image(logo, use_container_width=False, width=250)

# Título principal
st.title("📊 Resumen Anual de Ventas - Tierra Adentro Artesanal")
st.write("Análisis del desempeño de ventas, ingresos y tendencias anuales hasta Octubre 2024.")

# Cargar imágenes iniciales
cantidad_ventas_anual = Image.open("cantidad_ventas_anual.png")
ingresos_bruto = Image.open("ingresos_bruto.png")
ingresos_totales = Image.open("ingresos_totales.png")
cargo_impuesto = Image.open("cargo_impuesto.png")

# Distribuir visualizaciones en columnas
col1, col2 = st.columns([2, 2])

# Visualización 1: Cantidad de Ventas Anual
with col1:
    st.subheader("📈 Cantidad de Ventas Anual")
    st.image(cantidad_ventas_anual, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - Las ventas anuales han sufrido una **caída progresiva** desde 2021 (504) hasta 2024 (254).
        - Este descenso está alineado con la pérdida de poder adquisitivo debido a la inflación.
        - De cara a 2024, se proyecta una leve recuperación económica que podría estabilizar e incluso revertir parcialmente esta tendencia.
        """
    )

# Visualización 2: Ingresos Brutos Totales por Año
with col2:
    st.subheader("💰 Ingresos Brutos Totales por Año")
    st.image(ingresos_bruto, use_container_width=True)
    st.write(
        """
        **Análisis:**
        - A pesar de la merma en la cantidad de ventas, los **ingresos brutos crecieron**, impulsados por ajustes de precios ante la inflación.
        - La cifra más alta en 2024 (8.4 millones) refleja el impacto de la inflación más que un aumento real en la demanda.
        - Es fundamental diferenciar entre crecimiento nominal (por inflación) y crecimiento real (ajustado por poder adquisitivo).
        """
    )

# Visualización 3: Ingresos Totales por Año
st.subheader("🧾 Ingresos Totales por Año")
st.image(ingresos_totales, use_container_width=True)
st.write(
    """
    **Análisis:**
    - Los ingresos totales pasaron de $1.5M en 2021 a $5.7M en 2024, un incremento explicado principalmente por la inflación.
    - Este aumento no representa necesariamente una mejora del negocio en términos reales, sino una actualización de precios que acompaña la pérdida de valor de la moneda.
    - **Recomendación:** Ajustar la estrategia de costos y mejorar la eficiencia operativa para preservar la rentabilidad real.
    """
)

# Visualización 4: Cargo de Impuesto Mensual
st.subheader("📉 Cargo de Impuesto Mensual")
st.image(cargo_impuesto, use_container_width=True)
st.write(
    """
    **Análisis:**
    - La carga impositiva es significativa, impactando fuertemente sobre los márgenes.
    - En Septiembre, el cargo impositivo superó los $500K, reflejando la presión tributaria.
    - **Recomendación:** Explorar beneficios fiscales, exenciones y un calendario de pagos óptimo que reduzca el impacto impositivo y mejore el flujo de caja.
    """
)


# --------------------------
# Nuevas visualizaciones
# --------------------------

# Visualización 5: Ventas por Mes (2024)
st.subheader("📅 Ventas por Mes (2024)")
ventas_mes = Image.open("ventas_mes.png")
st.image(ventas_mes, use_container_width=True)
st.write(
    """
    **Análisis:**
    - La distribución mensual revela una marcada estacionalidad. Ciertos meses destacan por mayores transacciones (relacionadas con turismo, ferias artesanales o eventos culturales), mientras otros muestran contracción.
    - Incluso bajo el contexto inflacionario, las promociones puntuales, lanzamientos de productos y la exposición en eventos claves permiten mantener e impulsar la demanda.
    - **Recomendación:** Planificar el inventario y las estrategias de marketing con anticipación, maximizando la presencia publicitaria y las promociones en meses de alto tráfico. En meses bajos, implementar ofertas temáticas o descuentos especiales para mover el stock.
    """
)

# Visualización 6: Ventas por Día de la Semana (2024)
st.subheader("📆 Ventas por Día de la Semana (2024)")
ventas_semana = Image.open("ventas_semanas.png")
st.image(ventas_semana, use_container_width=True)
st.write(
    """
    **Análisis:**
    - El patrón semanal muestra mayores ventas hacia el fin de semana, probablemente debido a un aumento del consumo recreativo, el turismo interno y el tiempo libre de los clientes.
    - Los días laborales tienen un flujo más estable pero menor volumen, sugiriendo compras más planificadas y de menor ticket promedio.
    - **Recomendación:** Concentrar esfuerzos publicitarios y promociones flash en la víspera del fin de semana, ofrecer degustaciones, talleres cortos u ofertas especiales que motiven al cliente a concretar la compra. En días laborales, enfocar en la fidelización de clientes recurrentes, ventas corporativas y envíos a domicilio.
    """
)

# Visualización 7: Horas Pico de Venta (2024)
st.subheader("⏰ Horas Pico de Venta (2024)")
hora_pico_ventas = Image.open("hora_pico_ventas.png")
st.image(hora_pico_ventas, use_container_width=True)
st.write(
    """
    **Análisis:**
    - La demanda se concentra en determinadas franjas horarias, usualmente asociadas con momentos de ocio, salidas después del trabajo o descanso.
    - Identificar estas horas pico permite optimizar la experiencia del cliente, ofreciendo atención reforzada y promociones en las horas de mayor tráfico.
    - **Recomendación:** Ajustar la dotación de personal en las horas críticas, lanzar campañas publicitarias o descuentos relámpago en esos rangos, e incluso sincronizar publicaciones en redes sociales para aprovechar el tráfico máximo.
    """
)

# Resumen Final Integrado
st.write("---")
st.info(
    """
    **Resumen Final:**
    - El contexto inflacionario argentino ha reducido la cantidad de ventas, pero ha inflado los ingresos nominales por el ajuste de precios.
    - La carga impositiva y los costos crecientes exigen una gestión más eficiente para sostener la rentabilidad real.
    - Las nuevas visualizaciones aportan una comprensión granular:  
       - **Mensual:** Estacionalidad marcada, con meses pico y otros más débiles.
       - **Semanal:** Fines de semana con mayor dinamismo, días laborales más estables pero con menor ticket.
       - **Horaria:** Horas pico claras para orientar promociones y campañas segmentadas.
    - Con esta información, Tierra Adentro Artesanal puede optimizar su estrategia global, ajustando precios, promociones, inventario y campañas publicitarias para maximizar las ventas y la rentabilidad, incluso en un entorno económico desafiante.
    """
)

#streamlit run dashboard_resumen_anual.py


