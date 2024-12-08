import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Lista de conexiones
edges = [
    ('GPU', 'Pantalla negra'), ('Monitor', 'Pantalla negra'), ('SO', 'Pantalla negra'), ('PSU', 'Pantalla negra'),
    ('PSU', 'No enciende'), ('Motherboard', 'No enciende'), ('CPU', 'No enciende'),
    ('Motherboard', 'No detección'), ('GPU', 'No detección'), ('RAM', 'No detección'), ('Almacenamiento', 'No detección'),
    ('CPU', 'Falta de rendimiento'), ('RAM', 'Falta de rendimiento'), ('GPU', 'Falta de rendimiento'), ('SO', 'Falta de rendimiento'),
    ('GPU', 'Pixeles muertos'), ('Monitor', 'Pixeles muertos'),
    ('PSU', 'Sobreruido'), ('Ventiladores', 'Sobreruido'), ('Motherboard', 'Sobreruido'),
    ('CPU', 'Altas temperaturas'), ('GPU', 'Altas temperaturas'), ('PSU', 'Altas temperaturas'), ('Ventiladores', 'Altas temperaturas'),
    ('SO', 'Pantallazo azul'), ('RAM', 'Pantallazo azul'), ('CPU', 'Pantallazo azul'),
    ('SO', 'Inicio lento'), ('Almacenamiento', 'Inicio lento'), ('RAM', 'Inicio lento'),
    ('Motherboard', 'Pitido'), ('PSU', 'Pitido'),
    ('SO', 'Conexión lenta'), ('Almacenamiento', 'Conexión lenta'), ('CPU', 'Conexión lenta'),
    ('Motherboard', 'Mal funcionamiento USB'), ('SO', 'Mal funcionamiento USB'),
    ('SO', 'Cuelgues aleatorios'), ('RAM', 'Cuelgues aleatorios'), ('CPU', 'Cuelgues aleatorios'), ('Motherboard', 'Cuelgues aleatorios'),
    ('Almacenamiento', 'Fallos de guardado'), ('SO', 'Fallos de guardado'), ('RAM', 'Fallos de guardado'),
    ('Periferico', 'Mala detección perifericos'), ('SO', 'Mala detección perifericos'), ('Motherboard', 'Mala detección perifericos')
]

# Crear el grafo dirigido
G = nx.DiGraph()
G.add_edges_from(edges)

# Parámetros iniciales de visualización
initial_k = 0.5
initial_iterations = 50

# Función para dibujar la red con parámetros ajustables
def draw_network(k=initial_k, iterations=initial_iterations):
    plt.clf()  # Limpiar la figura
    pos = nx.spring_layout(G, seed=42, k=k, iterations=iterations)
    nx.draw(
        G, pos, with_labels=True, node_size=2000, node_color="lightblue",
        font_size=10, font_weight="bold", edge_color="gray"
    )
    plt.title("Visualización de la Red Bayesiana", fontsize=16)
    plt.draw()

# Configurar la figura
fig, ax = plt.subplots(figsize=(12, 10))
plt.subplots_adjust(bottom=0.25)  # Dejar espacio para los sliders

# Dibujar la red inicial
draw_network()

# Crear sliders para ajustar los parámetros
ax_k = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor="lightgray")
ax_iter = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor="lightgray")

slider_k = Slider(ax_k, "Espaciado (k)", 0.1, 1.0, valinit=initial_k, valstep=0.05)
slider_iter = Slider(ax_iter, "Iteraciones", 10, 100, valinit=initial_iterations, valstep=1)

# Función para actualizar la red
def update(val):
    k = slider_k.val
    iterations = int(slider_iter.val)
    draw_network(k, iterations)

slider_k.on_changed(update)
slider_iter.on_changed(update)

# Botón para reiniciar sliders
reset_ax = plt.axes([0.8, 0.9, 0.1, 0.04])
button_reset = Button(reset_ax, "Reiniciar", color="lightblue", hovercolor="gray")

def reset(event):
    slider_k.reset()
    slider_iter.reset()

button_reset.on_clicked(reset)

# Mostrar la visualización
plt.show()
