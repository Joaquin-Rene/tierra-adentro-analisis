from __future__ import annotations

from pathlib import Path
from typing import Iterable

import streamlit as st
from PIL import Image


ROOT_DIR = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT_DIR / "images"


def render_app() -> None:
    st.set_page_config(
        page_title="Tierra Adentro Artesanal | Dashboard de Negocio",
        page_icon="🌿",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_styles()
    render_sidebar()
    render_header()
    render_methodology()

    tab_portada, tab_ventas, tab_productos, tab_clientes, tab_envios, tab_plan = st.tabs(
        [
            "Visión general",
            "Ventas",
            "Productos",
            "Clientes",
            "Envíos",
            "Plan de acción",
        ]
    )

    with tab_portada:
        render_overview_tab()
    with tab_ventas:
        render_sales_tab()
    with tab_productos:
        render_products_tab()
    with tab_clientes:
        render_customers_tab()
    with tab_envios:
        render_shipping_tab()
    with tab_plan:
        render_action_tab()

    st.divider()
    st.markdown(
        """
        <div class="footer-note">
            Proyecto de portfolio orientado a negocio: combina storytelling ejecutivo, visualización
            y recomendaciones accionables a partir de datos comerciales, geográficos y operativos.
        </div>
        """,
        unsafe_allow_html=True,
    )


def inject_styles() -> None:
    st.markdown(
        """
        <style>
            :root {
                --sand: #f6efe6;
                --cream: #fbf7f2;
                --clay: #8f5d38;
                --earth: #59341d;
                --ink: #24170f;
                --olive: #7d8750;
                --line: rgba(89, 52, 29, 0.18);
            }

            .stApp {
                background:
                    radial-gradient(circle at top right, rgba(143, 93, 56, 0.12), transparent 22rem),
                    linear-gradient(180deg, #fcfaf7 0%, var(--sand) 100%);
            }

            .block-container {
                max-width: 1180px;
                padding-top: 2rem;
                padding-bottom: 2.5rem;
            }

            .eyebrow {
                font-size: 0.82rem;
                letter-spacing: 0.12rem;
                text-transform: uppercase;
                color: var(--clay);
                font-weight: 700;
                margin-bottom: 0.5rem;
            }

            .hero-copy {
                font-size: 1.05rem;
                line-height: 1.75;
                color: rgba(36, 23, 15, 0.88);
                margin-bottom: 0;
            }

            .info-card {
                background: rgba(251, 247, 242, 0.88);
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 1rem 1.1rem;
                min-height: 170px;
                box-shadow: 0 10px 30px rgba(89, 52, 29, 0.05);
            }

            .info-card h4 {
                margin: 0 0 0.6rem 0;
                color: var(--earth);
                font-size: 1rem;
            }

            .info-card p,
            .info-card li {
                color: rgba(36, 23, 15, 0.86);
                line-height: 1.65;
            }

            .section-label {
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.14rem;
                color: var(--olive);
                font-weight: 700;
                margin-bottom: 0.3rem;
            }

            .footer-note {
                color: rgba(36, 23, 15, 0.72);
                font-size: 0.95rem;
                line-height: 1.6;
            }

            [data-testid="stMetric"] {
                background: rgba(251, 247, 242, 0.9);
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 1rem 1.1rem;
                box-shadow: 0 10px 30px rgba(89, 52, 29, 0.05);
            }

            [data-testid="stMetricLabel"] {
                color: rgba(36, 23, 15, 0.72);
            }

            [data-testid="stMetricValue"] {
                color: var(--earth);
            }

            [data-testid="stSidebar"] {
                background: rgba(244, 233, 220, 0.9);
                border-right: 1px solid var(--line);
            }

            .stTabs [data-baseweb="tab-list"] {
                gap: 0.4rem;
            }

            .stTabs [data-baseweb="tab"] {
                background: rgba(251, 247, 242, 0.65);
                border-radius: 999px;
                border: 1px solid var(--line);
                padding: 0.4rem 0.9rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    st.sidebar.title("Tierra Adentro")
    st.sidebar.markdown(
        """
        Proyecto de portfolio sobre rentabilidad real, mix de productos, geografía de clientes
        y eficiencia operativa en Mercado Libre.
        """
    )
    st.sidebar.markdown("### Stack")
    st.sidebar.markdown("- Python\n- SQL / SQLite\n- Streamlit\n- Visualización geográfica\n- Storytelling de negocio")
    st.sidebar.markdown("### Estructura")
    st.sidebar.code(
        "data/\nimages/\nnotebooks/\nstreamlit_app/\nREADME.md",
        language="text",
    )
    st.sidebar.markdown("### Ejecutar")
    st.sidebar.code("streamlit run dashboard_tierra_adentro.py", language="bash")


def render_header() -> None:
    col_logo, col_copy = st.columns([1, 2.2], vertical_alignment="center")

    with col_logo:
        render_image("logo_tierra_adentro.PNG", width=240)

    with col_copy:
        st.markdown('<div class="eyebrow">Portfolio Project · Python · SQL · Streamlit</div>', unsafe_allow_html=True)
        st.title("Tierra Adentro Artesanal")
        st.markdown(
            """
            <p class="hero-copy">
                Dashboard ejecutivo para analizar desempeño comercial, concentración geográfica,
                logística y oportunidades de crecimiento de un emprendimiento artesanal argentino.
                La propuesta apunta a mostrar criterio analítico, sensibilidad de negocio y
                capacidad de transformar datos en decisiones.
            </p>
            """,
            unsafe_allow_html=True,
        )

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Ventas anuales", "504 → 254", "-49.6%")
    metric_2.metric("Plazo promedio", "5.09 días", "Operación mejorable")
    metric_3.metric("Mix ganador", "Sandalias", "Core del negocio")
    metric_4.metric("Mayor concentración", "CABA / Bs. As.", "Demanda urbana")


def render_methodology() -> None:
    with st.expander("Datos, alcance y criterio analítico"):
        st.markdown(
            """
            - **Fuente principal:** exportaciones operativas de Mercado Libre y base SQLite del proyecto.
            - **Horizonte temporal:** ventas históricas 2021-2024 y métricas operativas recientes.
            - **Ejes evaluados:** ventas, portafolio de productos, perfil geográfico de clientes y envíos.
            - **Objetivo:** detectar dónde se erosiona la rentabilidad y qué acciones pueden mejorar crecimiento, ticket promedio y experiencia del cliente.
            - **Valor de portfolio:** el caso no se limita a gráficos; traduce datos en hipótesis comerciales y líneas de acción concretas.
            """
        )


def render_overview_tab() -> None:
    st.markdown('<div class="section-label">Narrativa del proyecto</div>', unsafe_allow_html=True)
    st.subheader("Qué muestra este caso")
    card_1, card_2, card_3 = st.columns(3)
    with card_1:
        render_card(
            "Problema de negocio",
            [
                "Los ingresos nominales suben, pero las unidades vendidas caen.",
                "La presión impositiva y los costos obligan a mirar rentabilidad real, no solo facturación.",
            ],
        )
    with card_2:
        render_card(
            "Hipótesis central",
            [
                "El negocio tiene tracción en categorías y zonas específicas.",
                "Una mejor estrategia comercial y logística puede sostener margen y reforzar posicionamiento.",
            ],
        )
    with card_3:
        render_card(
            "Resultado esperado",
            [
                "Priorizar productos más rentables.",
                "Optimizar campañas y reforzar operación en zonas y horarios de mayor demanda.",
            ],
        )

    st.markdown('<div class="section-label">Canales y presencia de marca</div>', unsafe_allow_html=True)
    channel_1, channel_2 = st.columns(2)
    with channel_1:
        render_image(
            "instagram_portada.PNG",
            caption="Instagram como canal de posicionamiento, comunidad y validación estética.",
        )
    with channel_2:
        render_image(
            "ml_portada.PNG",
            caption="Mercado Libre como canal principal de conversión y monetización.",
        )

    st.markdown('<div class="section-label">Lectura ejecutiva</div>', unsafe_allow_html=True)
    st.markdown(
        """
        Tierra Adentro Artesanal combina identidad de marca, propuesta artesanal y evidencia de
        demanda real. El dashboard se diseñó para responder tres preguntas: qué sostiene el negocio,
        dónde se concentra el cliente y qué decisiones tienen mayor retorno probable.
        """
    )


def render_sales_tab() -> None:
    st.subheader("Ventas y presión sobre la rentabilidad")
    left, right = st.columns(2)
    with left:
        render_chart_block(
            "cantidad_ventas_anual.png",
            "Cantidad anual de ventas",
            [
                "La caída desde 2021 a 2024 sugiere contracción de demanda en unidades.",
                "El crecimiento nominal de precios no compensa por sí mismo el deterioro del volumen.",
            ],
        )
    with right:
        render_chart_block(
            "ingresos_bruto.png",
            "Ingresos brutos por año",
            [
                "El salto de facturación está explicado en gran parte por inflación y ajuste de precios.",
                "Para una lectura honesta del negocio conviene separar crecimiento nominal de mejora real.",
            ],
        )

    full_1, full_2 = st.columns(2)
    with full_1:
        render_chart_block(
            "ingresos_totales.png",
            "Ingresos netos o totales",
            [
                "El volumen monetario aumenta, pero con menor poder explicativo si no se ajusta por contexto.",
                "La lectura correcta es margen real y no solo facturación acumulada.",
            ],
        )
    with full_2:
        render_chart_block(
            "cargo_impuesto.png",
            "Carga impositiva mensual",
            [
                "La presión fiscal aparece como uno de los principales drenajes de margen.",
                "Esto vuelve crítica la revisión de precios, estructura de costos y planificación fiscal.",
            ],
        )

    season_1, season_2, season_3 = st.columns(3)
    with season_1:
        render_chart_block(
            "ventas_mes.png",
            "Estacionalidad mensual",
            [
                "Sirve para anticipar meses pico y ajustar campañas, stock y liquidez.",
            ],
        )
    with season_2:
        render_chart_block(
            "ventas_semanas.png",
            "Patrón semanal",
            [
                "Permite ubicar los días más activos y decidir cuándo empujar pauta o promociones.",
            ],
        )
    with season_3:
        render_chart_block(
            "hora_pico_ventas.png",
            "Horas pico de compra",
            [
                "La franja horaria correcta mejora timing de campañas y respuesta comercial.",
            ],
        )

    st.info(
        "Lectura ejecutiva: el negocio vende menos unidades, factura más por contexto inflacionario y necesita defender margen con pricing, costos y foco comercial."
    )


def render_products_tab() -> None:
    st.subheader("Productos, portafolio y oportunidades de mix")
    top_1, top_2 = st.columns(2)
    with top_1:
        render_chart_block(
            "conteo_tipo_producto.png",
            "Distribución por tipo de producto",
            [
                "Sandalias dominan el portafolio y concentran la identidad comercial.",
                "La diversificación existe, pero todavía cumple un rol secundario.",
            ],
        )
    with top_2:
        render_chart_block(
            "ingresos_productos.png",
            "Ingresos por categoría",
            [
                "La categoría principal explica la mayor parte de la facturación.",
                "Los accesorios aportan menor volumen, pero pueden mejorar el mix y el ticket promedio.",
            ],
        )

    mid_1, mid_2 = st.columns(2)
    with mid_1:
        render_chart_block(
            "sandalias_vendidas.png",
            "Modelos de sandalias más vendidos",
            [
                "Los productos ganadores validan una estética y un rango de precio específicos.",
                "Esto ayuda a decidir qué líneas reforzar y cuáles testear con lanzamientos limitados.",
            ],
        )
    with mid_2:
        render_chart_block(
            "top_10_productos_vendidos.png",
            "Top productos por unidades",
            [
                "La venta por volumen confirma el peso del core del negocio.",
                "También revela qué productos podrían funcionar como entrada a categorías nuevas.",
            ],
        )

    lower_1, lower_2 = st.columns(2)
    with lower_1:
        render_chart_block(
            "top_10_sincalzados.png",
            "Accesorios con mayor salida",
            [
                "Los no calzados agregan variedad y abren oportunidades de bundles o venta cruzada.",
            ],
        )
    with lower_2:
        render_chart_block(
            "top_10_masingresos.png",
            "Productos líderes en ingresos",
            [
                "Algunos accesorios premium muestran mejor relación ingreso/volumen.",
                "Eso sugiere una vía de expansión rentable más allá del producto principal.",
            ],
        )

    color_1, color_2 = st.columns(2)
    with color_1:
        render_chart_block(
            "distribucion_colores_productos.png",
            "Preferencias cromáticas",
            [
                "La paleta terrosa y oscura está alineada con el posicionamiento artesanal.",
            ],
        )
    with color_2:
        render_chart_block(
            "ingresos_colores_productos.png",
            "Ingresos por color",
            [
                "Conviene proteger stock en los tonos más rentables y usar colores especiales como test de mercado.",
            ],
        )

    st.info(
        "Lectura ejecutiva: sandalias sostienen el negocio, pero los accesorios premium ofrecen una palanca clara para diversificar margen y ticket promedio."
    )


def render_customers_tab() -> None:
    st.subheader("Geografía de clientes y perfil de demanda")
    center = st.columns([1, 2, 1])
    with center[1]:
        render_chart_block(
            "distribucion_provincias.png",
            "Distribución por provincia",
            [
                "Buenos Aires, CABA y Córdoba concentran la mayor tracción.",
                "Hay margen para una expansión geográfica selectiva basada en demanda ya validada.",
            ],
        )

    wide = st.columns([1, 5, 1])
    with wide[1]:
        render_chart_block(
            "distribucion_CABA.png",
            "Mapa de ventas en CABA",
            [
                "La concentración en barrios de alto poder adquisitivo orienta campañas, entregas y colaboraciones locales.",
            ],
            width=1000,
            use_container_width=False,
        )

    city_1, city_2 = st.columns(2)
    with city_1:
        render_chart_block(
            "top_10_ciudadesmasventas.png",
            "Ciudades con mayor volumen",
            [
                "Permite detectar focos de demanda fuera de CABA y priorizar expansión.",
            ],
        )
    with city_2:
        render_chart_block(
            "top_barrios_ventas.png",
            "Barrios con más ventas",
            [
                "Sirve para ajustar pauta geolocalizada y mejorar promesa logística.",
            ],
        )

    profile_1, profile_2 = st.columns(2)
    with profile_1:
        render_chart_block(
            "rango_dni.png",
            "Rango etario estimado",
            [
                "El público adulto concentra la demanda y ayuda a afinar tono, mensaje y propuesta de valor.",
            ],
        )
    with profile_2:
        render_chart_block(
            "clientes_compras.png",
            "Clientes con mayor recurrencia",
            [
                "La recompra todavía tiene espacio para crecer con mejores programas de fidelización.",
            ],
        )

    st.info(
        "Lectura ejecutiva: el negocio ya tiene hotspots claros; el siguiente paso es explotar mejor esos territorios con marketing geolocalizado y propuestas de fidelización."
    )


def render_shipping_tab() -> None:
    st.subheader("Operación logística y experiencia del cliente")
    ship_1, ship_2, ship_3 = st.columns(3)
    with ship_1:
        render_chart_block(
            "promedio_entrega.png",
            "Tiempo promedio de entrega",
            [
                "Un plazo cercano a 5 días es razonable, pero todavía mejorable frente a expectativas de e-commerce.",
            ],
        )
    with ship_2:
        render_chart_block(
            "envios_tiempo.png",
            "Intervalo horario de envíos",
            [
                "La concentración vespertina puede esconder cuellos de botella operativos.",
            ],
        )
    with ship_3:
        render_chart_block(
            "envios_semana.png",
            "Envíos por día de semana",
            [
                "Los picos de lunes y miércoles justifican planificación y capacidad específica.",
            ],
        )

    recommendations_1, recommendations_2 = st.columns(2)
    with recommendations_1:
        render_card(
            "Qué haría a corto plazo",
            [
                "Refuerzo operativo en días y franjas horarias de mayor carga.",
                "Seguimiento más visible para el cliente y revisión del SLA por zona.",
            ],
        )
    with recommendations_2:
        render_card(
            "Qué medir después",
            [
                "Entregas por transportista.",
                "Costo por envío y reclamos por demora.",
                "Promesa vs. entrega real en zonas premium.",
            ],
        )

    st.info(
        "Lectura ejecutiva: la logística no luce rota, pero sí suficientemente concentrada como para convertirse en un problema si aumenta la demanda."
    )


def render_action_tab() -> None:
    st.subheader("Plan de acción para crecer con mejor margen")
    action_1, action_2, action_3 = st.columns(3)
    with action_1:
        render_card(
            "Pricing y rentabilidad",
            [
                "Revisar costos reales y elasticidad por categoría.",
                "Diferenciar precios entre productos core y accesorios premium.",
                "Separar análisis nominal de análisis real.",
            ],
        )
    with action_2:
        render_card(
            "Marketing y adquisición",
            [
                "Reforzar Instagram como narrativa de marca y Mercado Libre como canal de conversión.",
                "Activar pauta geolocalizada en CABA, GBA y plazas ya validadas.",
                "Usar bundles para empujar ticket promedio.",
            ],
        )
    with action_3:
        render_card(
            "Operación y fidelización",
            [
                "Priorizar envíos en hotspots de alto valor.",
                "Diseñar acciones de recompra y beneficios para clientes recurrentes.",
                "Medir cohortes, recurrencia y performance por zona.",
            ],
        )

    st.markdown("### Próximas mejoras analíticas")
    st.markdown(
        """
        - Integrar métricas de Instagram para correlacionar contenido con ventas.
        - Construir un tablero de rentabilidad real por producto o familia.
        - Incorporar reseñas y devoluciones para enriquecer la lectura comercial.
        - Automatizar actualización mensual para transformar el caso en una demo viva.
        """
    )
    st.success(
        "El mayor valor del proyecto no es solo mostrar gráficos: es demostrar criterio para conectar señales comerciales, contexto económico y decisiones accionables."
    )


def render_card(title: str, bullets: Iterable[str]) -> None:
    bullet_items = "".join(f"<li>{item}</li>" for item in bullets)
    st.markdown(
        f"""
        <div class="info-card">
            <h4>{title}</h4>
            <ul>{bullet_items}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chart_block(
    image_name: str,
    title: str,
    bullets: Iterable[str],
    *,
    caption: str | None = None,
    width: int | None = None,
    use_container_width: bool = True,
) -> None:
    st.markdown(f"#### {title}")
    render_image(
        image_name,
        caption=caption,
        width=width,
        use_container_width=use_container_width,
    )
    for bullet in bullets:
        st.markdown(f"- {bullet}")


@st.cache_resource(show_spinner=False)
def load_image(image_name: str) -> Image.Image | None:
    image_path = IMAGES_DIR / image_name
    if not image_path.exists():
        return None
    with Image.open(image_path) as image:
        return image.copy()


def render_image(
    image_name: str,
    *,
    caption: str | None = None,
    width: int | None = None,
    use_container_width: bool = True,
) -> None:
    image = load_image(image_name)
    if image is None:
        st.warning(f"No se encontró el asset `{image_name}` en la carpeta `images/`.")
        return
    st.image(image, caption=caption, width=width, use_container_width=use_container_width)
