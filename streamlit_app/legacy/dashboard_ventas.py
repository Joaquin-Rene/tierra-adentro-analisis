import matplotlib.pyplot as plt
from PIL import Image
import os

# Directorio donde se encuentran las imágenes
directorio_imagenes = r"C:\Users\Pilar\Desktop\Joaquin\curso python\Dashboard e historias"

# Nombres de los archivos de imágenes
imagenes = {
    "cantidad_ventas_anual": "cantidad_ventas_anual.png",
    "cargo_impuesto": "cargo_impuesto.png",
    "hora_pico_ventas": "hora_pico_ventas.png",
    "ingresos_bruto": "ingresos_bruto.png",
    "ingresos_totales": "ingresos_totales.png",
    "promedio_general": "promedio_general.png",
    "promedio_mensual": "promedio_mensual.png",
    "ventas_mes": "ventas_mes.png",
    "ventas_semanas": "ventas_semanas.png",
}

# Función para cargar las imágenes usando Pillow
def cargar_imagen(nombre):
    ruta = os.path.join(directorio_imagenes, nombre)
    try:
        return Image.open(ruta)
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen '{ruta}'")
        return None

# Cargar todas las imágenes
imagenes_cargadas = {key: cargar_imagen(value) for key, value in imagenes.items()}

# Configurar el dashboard
fig, axes = plt.subplots(3, 3, figsize=(18, 12))  # 3 filas, 3 columnas
fig.suptitle("Dashboard de Ventas", fontsize=20, weight='bold', color='#5c4228', backgroundcolor='#f6efdf', y=0.95)

# Asignar cada imagen a una posición del dashboard
imagenes_ordenadas = [
    "cantidad_ventas_anual", "cargo_impuesto", "hora_pico_ventas",
    "ingresos_bruto", "ingresos_totales", "promedio_general",
    "promedio_mensual", "ventas_mes", "ventas_semanas"
]

for ax, img_key in zip(axes.ravel(), imagenes_ordenadas):
    imagen = imagenes_cargadas.get(img_key)
    if imagen:
        ax.imshow(imagen)
        ax.axis('off')  # Eliminar ejes
        ax.set_title(img_key.replace("_", " ").capitalize(), fontsize=10, weight='bold')

# Ajustar el layout
plt.tight_layout(rect=[0, 0, 1, 0.93])  # Espacio para el título principal
plt.show()



