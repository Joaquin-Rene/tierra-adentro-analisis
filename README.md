# Tierra Adentro Artesanal

Business analytics case for an Argentinian handcrafted ecommerce operation selling through Mercado Libre and Instagram. The project combines Python, SQL, SQLite, and Streamlit to turn commercial data into business-facing insights on profitability, product mix, customer geography, and logistics.

## Why this project matters

- It goes beyond charts and connects data to pricing, marketing, logistics, and retention decisions.
- It frames nominal revenue growth against inflation, focusing on real business performance.
- It shows an end-to-end analytics workflow: raw data, relational modeling, validation, dashboarding, and strategic recommendations.
- It is structured as a portfolio-ready case for recruiters, hiring managers, and client-facing conversations.

## App

- Live demo: [Open Streamlit app](https://tierra-adentro-dashboard.streamlit.app/)
- Local run:

```bash
pip install -r requirements.txt
streamlit run streamlit_app/dashboard_tierra_adentro.py
```

## Key business insights

- Units sold decline sharply between 2021 and 2024, while nominal revenue grows in an inflationary context.
- Sandals remain the commercial core, but premium accessories emerge as a profitable diversification path.
- Demand is concentrated in CABA, Buenos Aires, and selected urban areas across the country.
- Delivery performance is reasonable, but time-slot concentration suggests future operational bottlenecks if volume grows.

## Preview

### Main sales channel
![Mercado Libre storefront](images/ml_portada.PNG)

### Sales evolution
![Annual sales volume](images/cantidad_ventas_anual.png)

### Customer concentration in CABA
![Sales distribution in CABA](images/distribucion_CABA.png)

## Dashboard scope

- **Overview:** business context, channels, and executive framing
- **Sales:** yearly evolution, revenue, seasonality, and peak hours
- **Products:** category mix, top sellers, revenue by product, and color preferences
- **Customers:** geographic concentration, CABA hotspots, and demand profile
- **Shipping:** average delivery time, shipping distribution, and weekly workload
- **Action plan:** concrete business recommendations to improve margin and growth

## Stack

- Python
- Streamlit
- SQL / SQLite
- Pillow
- Jupyter Notebook

## Project structure

```text
.
|-- data/
|-- images/
|-- notebooks/
|-- streamlit_app/
|   |-- app.py
|   `-- legacy/
|-- dashboard_tierra_adentro.py
|-- README.md
`-- requirements.txt
```

## Portfolio value

This repository is designed to communicate three things clearly:

1. Technical ability to organize an analytics project from raw data to a presentable deliverable.
2. Business judgment to turn visualizations into concrete hypotheses and recommendations.
3. Product and presentation sensibility strong enough for GitHub, LinkedIn, and recruiter-facing portfolio reviews.
