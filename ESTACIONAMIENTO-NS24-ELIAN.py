import matplotlib.pyplot as plt
import numpy as np

# Función para crear el plano del estacionamiento
def crear_plano_estacionamiento():
    # Dimensiones del estacionamiento
    largo_total = 60  # en metros
    alto_total = 5    # en metros

    # Dimensiones de cada espacio
    ancho_espacio = 2.5  # en metros
    alto_espacio = 5     # en metros
    angulo_inclinacion = 25  # grados

    # Cálculo de la proyección horizontal de cada espacio de estacionamiento
    proyeccion_horizontal = ancho_espacio / np.cos(np.radians(angulo_inclinacion))

    # Número de espacios completos que caben en el largo total
    num_espacios = int(largo_total / proyeccion_horizontal)

    # Creación del plano
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, largo_total)
    ax.set_ylim(0, alto_total)

    # Dibujar cada espacio de estacionamiento
    for i in range(num_espacios):
        x = i * proyeccion_horizontal
        # Coordenadas del rectángulo inclinado
        rectangulo = np.array([
            [x, 0],
            [x + ancho_espacio * np.cos(np.radians(angulo_inclinacion)), ancho_espacio * np.sin(np.radians(angulo_inclinacion))],
            [x + ancho_espacio * np.cos(np.radians(angulo_inclinacion)) - alto_espacio * np.sin(np.radians(angulo_inclinacion)),
             alto_espacio * np.cos(np.radians(angulo_inclinacion)) + ancho_espacio * np.sin(np.radians(angulo_inclinacion))],
            [x - alto_espacio * np.sin(np.radians(angulo_inclinacion)), alto_espacio * np.cos(np.radians(angulo_inclinacion))]
        ])
        ax.add_patch(plt.Polygon(rectangulo, closed=True, fill=None, edgecolor='b'))

    # Agregar ángulo de inclinación al gráfico
    ax.text(0.5, 1.15, f'Ángulo de inclinación: {angulo_inclinacion}°', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)

    # Agregar etiquetas y mostrar el plano
    ax.set_xlabel('Largo (m)')
    ax.set_ylabel('Alto (m)')
    ax.set_title('Plano del Estacionamiento Núcleo Sepec v2', pad=40)  # Aumenta el espacio del título desde el borde superior
    ax.text(0.5, 0.5, 'soportevh@nucleosepec.com.mx', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8, color='gray')
  
    plt.grid(True)
    plt.tight_layout()  # Ajusta automáticamente el espaciado de la figura
    plt.savefig('plano_estacionamiento.png')  # Guardar la gráfica en un archivo
    plt.show()

# Ejecutar la función
if __name__ == "__main__":
    crear_plano_estacionamiento()
