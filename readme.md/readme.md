# 📊 Análisis de Rentabilidad – Tierra Adentro Artesanal

Proyecto de **Data Analytics** que evalúa ventas, costos y márgenes de un emprendimiento argentino de calzado y accesorios de cuero que opera en Mercado Libre (enero – octubre 2024).  
Incluye limpieza de datos en Python, modelado SQL, visualizaciones y un dashboard interactivo en Streamlit.

---

## 🎯 Objetivo

1. Medir **rentabilidad 2024** (ingresos, costos, impuestos, margen).  
2. Detectar productos, colores y horarios más rentables.  
3. Analizar distribución geográfica y comportamiento de clientes.  
4. Evaluar tiempos y eficiencia de envíos.  
5. Proponer acciones de mejora (precios, marketing, logística).

---

## 🗂️ Estructura del repositorio

tierra-adentro-analisis/ ├── notebooks/ │ └── proyecto_tierra_adentro.ipynb ├── streamlit_app/ │ └── dashboard_tierra_adentro.py ├── images/ ├── data/ │ ├── raw/ │ │ └── ventas_original.xlsx │ └── processed/ │ └── ventas_publico.xlsx └── requirements.txt


> **Privacidad** Las columnas con datos personales (Nombre, DNI, Domicilio) se eliminaron; los archivos compartidos solo contienen información anonimizada.

---

## ⚙️ Instalación rápida

```bash
# (opcional) crear entorno virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt


🚀 Cómo ejecutar
1. Notebook
jupyter lab notebooks/proyecto_tierra_adentro.ipynb
Sigue el índice del notebook (limpieza → SQL → visualizaciones).
Usa automáticamente data/processed/ventas_publico.xlsx.

2. Dashboard Streamlit

cd streamlit_app
streamlit run dashboard_tierra_adentro.py
Se abrirá en http://localhost:8501 con seis pestañas: Portada, Ventas, Publicaciones, Clientes, Envíos y Propuesta de Mejoras.

🔎 Metodología (resumen)

Fase	Descripción
Limpieza	13 pasos: eliminación de columnas irrelevantes, corrección de fechas, normalización de textos, extracción de atributos (color, talle), tipado final.
Base SQLite	4 tablas (venta, publicacion, clientes, envios) con claves foráneas y tipos de datos definidos.
Consultas SQL	KPIs de ingresos, costos, unidades vendidas, tiempos de entrega, tendencias horarias y geográficas.
Visualizaciones	22 gráficos (tendencias anuales, ventas por mes, colores más vendidos, mapa de provincias, etc.).
Dashboard	Streamlit “single‑page app” con pestañas, imágenes y conclusiones narradas.
📈 Resultados destacados

Insight (ene‑oct 2024)	Valor
Ingresos nominales	ARS 5,7 M (⇧ +280 % vs. 2021)
Unidades vendidas	254 pares (⇩ –50 % vs. 2021)
Producto estrella	Sandalias de cuero (60 % de ingresos)
Tiempo medio de entrega	5 días • picos lunes/miércoles
Región top	CABA + Buenos Aires (≈ 70 % de ventas)
Consulta la pestaña Propuesta de Mejoras del dashboard para acciones de precios, marketing e inventario.

---
 *Este proyecto fue realizado de forma independiente como muestra de mis habilidades en análisis de datos aplicado a e-commerce. Está disponible en este repositorio únicamente con fines de portafolio*
