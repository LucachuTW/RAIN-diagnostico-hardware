from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir el modelo de red bayesiana y sus relaciones
model = BayesianNetwork([
    ('GPU', 'Pantalla negra'), ('Monitor', 'Pantalla negra'), ('SO', 'Pantalla negra'), ('PSU', 'Pantalla negra'),
    ('PSU', 'No enciende'), ('Motherboard', 'No enciende'), ('CPU', 'No enciende'),
    ('Motherboard', 'No señal'), ('GPU', 'No señal'), ('CPU', 'No señal'),
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
    ('Monitor', 'Desplazamiento pantalla'), ('GPU', 'Desplazamiento pantalla'),
    ('SO', 'Cuelgues aleatorios'), ('RAM', 'Cuelgues aleatorios'), ('CPU', 'Cuelgues aleatorios'), ('Motherboard', 'Cuelgues aleatorios'),
    ('Almacenamiento', 'Fallos de guardado'), ('SO', 'Fallos de guardado'), ('RAM', 'Fallos de guardado'),
    ('Mouse', 'Mala detección ratón'), ('SO', 'Mala detección ratón'), ('Motherboard', 'Mala detección ratón'),
    ('Keyboard', 'Mala detección teclas'), ('SO', 'Mala detección teclas'), ('Motherboard', 'Mala detección teclas')
])

# Definir CPDs para los componentes (probabilidad base)
cpd_gpu = TabularCPD(variable='GPU', variable_card=2, values=[[0.5], [0.5]])
cpd_cpu = TabularCPD(variable='CPU', variable_card=2, values=[[0.5], [0.5]])
cpd_monitor = TabularCPD(variable='Monitor', variable_card=2, values=[[0.5], [0.5]])
cpd_psu = TabularCPD(variable='PSU', variable_card=2, values=[[0.5], [0.5]])
cpd_motherboard = TabularCPD(variable='Motherboard', variable_card=2, values=[[0.5], [0.5]])
cpd_ram = TabularCPD(variable='RAM', variable_card=2, values=[[0.5], [0.5]])
cpd_so = TabularCPD(variable='SO', variable_card=2, values=[[0.5], [0.5]])
cpd_almacenamiento = TabularCPD(variable='Almacenamiento', variable_card=2, values=[[0.5], [0.5]])
cpd_ventiladores = TabularCPD(variable='Ventiladores', variable_card=2, values=[[0.5], [0.5]])
cpd_mouse = TabularCPD(variable='Mouse', variable_card=2, values=[[0.5], [0.5]])
cpd_keyboard = TabularCPD(variable='Keyboard', variable_card=2, values=[[0.5], [0.5]])

# Definir CPDs para cada problema usando los datos proporcionados
cpd_pantalla_negra = TabularCPD(
    variable='Pantalla negra', variable_card=2,
    values=[[0.6, 0.6, 0.9, 0.6, 0.9, 0.6, 0.6, 0.9, 0.6, 0.6, 0.9, 0.6, 0.9, 0.6, 0.6, 0.9],
            [0.4, 0.4, 0.1, 0.4, 0.1, 0.4, 0.4, 0.1, 0.4, 0.4, 0.1, 0.4, 0.1, 0.4, 0.4, 0.1]],
    evidence=['GPU', 'Monitor', 'SO', 'PSU'], evidence_card=[2, 2, 2, 2]
)

cpd_no_enciende = TabularCPD(
    variable='No enciende', variable_card=2,
    values=[[0.5, 0.5, 0.7, 0.5, 0.5, 0.7, 0.5, 0.7],
            [0.5, 0.5, 0.3, 0.5, 0.5, 0.3, 0.5, 0.3]],
    evidence=['PSU', 'Motherboard', 'CPU'], evidence_card=[2, 2, 2]
)

cpd_no_senal = TabularCPD(
    variable='No señal', variable_card=2,
    values=[[0.5, 0.7, 0.7, 0.5, 0.7, 0.5, 0.5, 0.3],
            [0.5, 0.3, 0.3, 0.5, 0.3, 0.5, 0.5, 0.7]],
    evidence=['Motherboard', 'GPU', 'CPU'], evidence_card=[2, 2, 2]
)

cpd_no_deteccion = TabularCPD(
    variable='No detección', variable_card=2,
    values=[[0.6, 0.6, 0.8, 0.7, 0.7, 0.5, 0.5, 0.9, 0.6, 0.6, 0.8, 0.7, 0.7, 0.5, 0.5, 0.9],
            [0.4, 0.4, 0.2, 0.3, 0.3, 0.5, 0.5, 0.1, 0.4, 0.4, 0.2, 0.3, 0.3, 0.5, 0.5, 0.1]],
    evidence=['Motherboard', 'GPU', 'RAM', 'Almacenamiento'], evidence_card=[2, 2, 2, 2]
)

cpd_falta_rendimiento = TabularCPD(
    variable='Falta de rendimiento', variable_card=2,
    values=[[0.6, 0.6, 0.8, 0.6, 0.8, 0.5, 0.6, 0.8, 0.6, 0.6, 0.8, 0.6, 0.8, 0.5, 0.6, 0.8],
            [0.4, 0.4, 0.2, 0.4, 0.2, 0.5, 0.4, 0.2, 0.4, 0.4, 0.2, 0.4, 0.2, 0.5, 0.4, 0.2]],
    evidence=['CPU', 'RAM', 'GPU', 'SO'], evidence_card=[2, 2, 2, 2]
)

cpd_pixeles_muertos = TabularCPD(
    variable='Pixeles muertos', variable_card=2,
    values=[[0.8, 0.9, 0.8, 0.5],
            [0.2, 0.1, 0.2, 0.5]],
    evidence=['GPU', 'Monitor'], evidence_card=[2, 2]
)

cpd_sobreruido = TabularCPD(
    variable='Sobreruido', variable_card=2,
    values=[[0.5, 0.4, 0.4, 0.3, 0.3, 0.4, 0.5, 0.5],
            [0.5, 0.6, 0.6, 0.7, 0.7, 0.6, 0.5, 0.5]],
    evidence=['PSU', 'Ventiladores', 'Motherboard'], evidence_card=[2, 2, 2]
)

# Corrección del CPD de altas temperaturas
cpd_altas_temperaturas = TabularCPD(
    variable='Altas temperaturas', variable_card=2,
    values=[[0.7, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.7, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]],
    evidence=['CPU', 'GPU', 'PSU', 'Ventiladores'], evidence_card=[2, 2, 2, 2]
)

cpd_pantallazo_azul = TabularCPD(
    variable='Pantallazo azul', variable_card=2,
    values=[[0.5, 0.6, 0.5, 0.5, 0.6, 0.5, 0.4, 0.4],
            [0.5, 0.4, 0.5, 0.5, 0.4, 0.5, 0.6, 0.6]],
    evidence=['SO', 'RAM', 'CPU'], evidence_card=[2, 2, 2]
)

cpd_inicio_lento = TabularCPD(
    variable='Inicio lento', variable_card=2,
    values=[[0.5, 0.5, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5],
            [0.5, 0.5, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5]],
    evidence=['SO', 'Almacenamiento', 'RAM'], evidence_card=[2, 2, 2]
)

cpd_pitido = TabularCPD(
    variable='Pitido', variable_card=2,
    values=[[0.5, 0.6, 0.5, 0.4],
            [0.5, 0.4, 0.5, 0.6]],
    evidence=['Motherboard', 'PSU'], evidence_card=[2, 2]
)

# Corrección del CPD de conexión lenta
cpd_conexion_lenta = TabularCPD(
    variable='Conexión lenta', variable_card=2,
    values=[[0.5, 0.6, 0.5, 0.4, 0.6, 0.4, 0.5, 0.6],
            [0.5, 0.4, 0.5, 0.6, 0.4, 0.6, 0.5, 0.4]],
    evidence=['SO', 'Almacenamiento', 'CPU'], evidence_card=[2, 2, 2]
)

cpd_mal_funcionamiento_usb = TabularCPD(
    variable='Mal funcionamiento USB', variable_card=2,
    values=[[0.5, 0.4, 0.6, 0.5],
            [0.5, 0.6, 0.4, 0.5]],
    evidence=['Motherboard', 'SO'], evidence_card=[2, 2]
)

cpd_desplazamiento_pantalla = TabularCPD(
    variable='Desplazamiento pantalla', variable_card=2,
    values=[[0.5, 0.4, 0.5, 0.6],
            [0.5, 0.6, 0.5, 0.4]],
    evidence=['Monitor', 'GPU'], evidence_card=[2, 2]
)

cpd_cuelgues_aleatorios = TabularCPD(
    variable='Cuelgues aleatorios', variable_card=2,
    values=[[0.5, 0.6, 0.5, 0.4, 0.5, 0.6, 0.5, 0.4, 0.5, 0.6, 0.5, 0.4, 0.5, 0.6, 0.5, 0.4],
            [0.5, 0.4, 0.5, 0.6, 0.5, 0.4, 0.5, 0.6, 0.5, 0.4, 0.5, 0.6, 0.5, 0.4, 0.5, 0.6]],
    evidence=['SO', 'RAM', 'CPU', 'Motherboard'], evidence_card=[2, 2, 2, 2]
)

cpd_fallos_guardado = TabularCPD(
    variable='Fallos de guardado', variable_card=2,
    values=[[0.5, 0.6, 0.5, 0.4, 0.5, 0.5, 0.5, 0.6],
            [0.5, 0.4, 0.5, 0.6, 0.5, 0.5, 0.5, 0.4]],
    evidence=['Almacenamiento', 'SO', 'RAM'], evidence_card=[2, 2, 2]
)

cpd_mala_deteccion_raton = TabularCPD(
    variable='Mala detección ratón', variable_card=2,
    values=[[0.5, 0.4, 0.6, 0.5, 0.5, 0.4, 0.6, 0.5],
            [0.5, 0.6, 0.4, 0.5, 0.5, 0.6, 0.4, 0.5]],
    evidence=['Mouse', 'SO', 'Motherboard'], evidence_card=[2, 2, 2]
)

cpd_mala_deteccion_teclas = TabularCPD(
    variable='Mala detección teclas', variable_card=2,
    values=[[0.5, 0.6, 0.4, 0.5, 0.5, 0.6, 0.4, 0.5],
            [0.5, 0.4, 0.6, 0.5, 0.5, 0.4, 0.6, 0.5]],
    evidence=['Keyboard', 'SO', 'Motherboard'], evidence_card=[2, 2, 2]
)

# Agregar todos los CPDs al modelo
model.add_cpds(
    cpd_gpu, cpd_cpu, cpd_monitor, cpd_psu, cpd_motherboard, cpd_ram,
    cpd_so, cpd_almacenamiento, cpd_ventiladores, cpd_mouse, cpd_keyboard,
    cpd_pantalla_negra, cpd_no_enciende, cpd_no_senal, cpd_no_deteccion,
    cpd_falta_rendimiento, cpd_pixeles_muertos, cpd_sobreruido, cpd_altas_temperaturas,
    cpd_pantallazo_azul, cpd_inicio_lento, cpd_pitido, cpd_conexion_lenta,
    cpd_mal_funcionamiento_usb, cpd_desplazamiento_pantalla, cpd_cuelgues_aleatorios,
    cpd_fallos_guardado, cpd_mala_deteccion_raton, cpd_mala_deteccion_teclas
)

# Verificar que el modelo es consistente
assert model.check_model()

# Realizar inferencia
infer = VariableElimination(model)

# Consultar probabilidad de 'Pantalla negra' dado que 'GPU' y 'Monitor' están en estado 1
result = infer.query(variables=['Pantalla negra'], evidence={'GPU': 1, 'Monitor': 1})

print(result)