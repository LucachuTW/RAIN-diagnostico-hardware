from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Definir el modelo y las conexiones
model = BayesianNetwork([
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
])

list_evidences = ["Pantalla negra", "No enciende", "No detección", "Falta de rendimiento", "Pixeles muertos", 
                  "Sobreruido", "Altas temperaturas", "Pantallazo azul", "Inicio lento", "Pitido", "Conexión lenta", 
                  "Mal funcionamiento USB", "Cuelgues aleatorios", "Fallos de guardado", "Mala detección perifericos"]

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
cpd_periferico = TabularCPD(variable='Periferico', variable_card=2, values=[[0.5], [0.5]])

# Definir CPDs para cada problema usando los datos proporcionados
cpd_pantalla_negra = TabularCPD(
    variable='Pantalla negra', variable_card=2,
    values=[[0.9, 0.7, 0.95, 0.8, 0.85, 0.7, 0.8, 0.95, 0.75, 0.7, 0.9, 0.7, 0.9, 0.8, 0.8, 0.95],
            [0.1, 0.3, 0.05, 0.2, 0.15, 0.3, 0.2, 0.05, 0.25, 0.3, 0.1, 0.3, 0.1, 0.2, 0.2, 0.05]],
    evidence=['GPU', 'Monitor', 'SO', 'PSU'], evidence_card=[2, 2, 2, 2]
)


cpd_no_enciende = TabularCPD(
    variable='No enciende', variable_card=2,
    values=[[0.9, 0.8, 0.85, 0.7, 0.8, 0.85, 0.7, 0.6],
            [0.1, 0.2, 0.15, 0.3, 0.2, 0.15, 0.3, 0.4]],
    evidence=['PSU', 'Motherboard', 'CPU'], evidence_card=[2, 2, 2]
)



cpd_no_deteccion = TabularCPD(
    variable='No detección', variable_card=2,
    values=[[0.85, 0.75, 0.9, 0.8, 0.7, 0.6, 0.6, 0.95, 0.8, 0.7, 0.85, 0.8, 0.9, 0.65, 0.7, 0.95],
            [0.15, 0.25, 0.1, 0.2, 0.3, 0.4, 0.4, 0.05, 0.2, 0.3, 0.15, 0.2, 0.1, 0.35, 0.3, 0.05]],
    evidence=['Motherboard', 'GPU', 'RAM', 'Almacenamiento'], evidence_card=[2, 2, 2, 2]
)


cpd_falta_rendimiento = TabularCPD(
    variable='Falta de rendimiento', variable_card=2,
    values=[[0.85, 0.6, 0.9, 0.7, 0.8, 0.65, 0.75, 0.85, 0.8, 0.75, 0.9, 0.8, 0.85, 0.65, 0.7, 0.9],
            [0.15, 0.4, 0.1, 0.3, 0.2, 0.35, 0.25, 0.15, 0.2, 0.25, 0.1, 0.2, 0.15, 0.35, 0.3, 0.1]],
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
    values=[[0.5, 0.4, 0.4, 0.3, 0.3, 0.4, 0.2, 0.6],
            [0.5, 0.6, 0.6, 0.7, 0.7, 0.6, 0.8, 0.4]],
    evidence=['PSU', 'Ventiladores', 'Motherboard'], evidence_card=[2, 2, 2]
)

cpd_altas_temperaturas = TabularCPD(
    variable='Altas temperaturas', variable_card=2,
    values=[[0.9, 0.8, 0.7, 0.6, 0.75, 0.65, 0.8, 0.7, 0.85, 0.75, 0.6, 0.7, 0.8, 0.65, 0.75, 0.7],
            [0.1, 0.2, 0.3, 0.4, 0.25, 0.35, 0.2, 0.3, 0.15, 0.25, 0.4, 0.3, 0.2, 0.35, 0.25, 0.3]],
    evidence=['CPU', 'GPU', 'PSU', 'Ventiladores'], evidence_card=[2, 2, 2, 2]
)


cpd_pantallazo_azul = TabularCPD(
    variable='Pantallazo azul', variable_card=2,
    values=[[0.8, 0.6, 0.8, 0.5, 0.6, 0.3, 0.4, 0.4],
            [0.2, 0.4, 0.2, 0.5, 0.4, 0.7, 0.6, 0.6]],
    evidence=['SO', 'RAM', 'CPU'], evidence_card=[2, 2, 2]
)

cpd_inicio_lento = TabularCPD(
    variable='Inicio lento', variable_card=2,
    values=[[0.7, 0.6, 0.6, 0.5, 0.5, 0.8, 0.6, 0.7],
            [0.3, 0.4, 0.4, 0.5, 0.5, 0.2, 0.4, 0.3]],
    evidence=['SO', 'Almacenamiento', 'RAM'], evidence_card=[2, 2, 2]
)

cpd_pitido = TabularCPD(
    variable='Pitido', variable_card=2,
    values=[[0.8, 0.6, 0.7, 0.4],
            [0.2, 0.4, 0.3, 0.6]],
    evidence=['Motherboard', 'PSU'], evidence_card=[2, 2]
)

cpd_conexion_lenta = TabularCPD(
    variable='Conexión lenta', variable_card=2,
    values=[[0.5, 0.6, 0.5, 0.4, 0.6, 0.4, 0.5, 0.6],
            [0.5, 0.4, 0.5, 0.6, 0.4, 0.6, 0.5, 0.4]],
    evidence=['SO', 'Almacenamiento', 'CPU'], evidence_card=[2, 2, 2]
)

cpd_mal_funcionamiento_usb = TabularCPD(
    variable='Mal funcionamiento USB', variable_card=2,
    values=[[0.85, 0.6, 0.75, 0.5],
            [0.15, 0.4, 0.25, 0.5]],
    evidence=['Motherboard', 'SO'], evidence_card=[2, 2]
)


cpd_cuelgues_aleatorios = TabularCPD(
    variable='Cuelgues aleatorios', variable_card=2,
    values=[[0.9, 0.7, 0.3, 0.5, 0.6, 0.8, 0.6, 0.5, 0.7, 0.8, 0.6, 0.5, 0.3, 0.85, 0.6, 0.4],
            [0.1, 0.3, 0.7, 0.5, 0.4, 0.2, 0.4, 0.5, 0.3, 0.2, 0.4, 0.5, 0.7, 0.15, 0.4, 0.6]],
    evidence=['SO', 'RAM', 'CPU', 'Motherboard'], evidence_card=[2, 2, 2, 2]
)


cpd_fallos_guardado = TabularCPD(
    variable='Fallos de guardado', variable_card=2,
    values=[[0.9, 0.7, 0.8, 0.6, 0.7, 0.85, 0.75, 0.8],
            [0.1, 0.3, 0.2, 0.4, 0.3, 0.15, 0.25, 0.2]],
    evidence=['Almacenamiento', 'SO', 'RAM'], evidence_card=[2, 2, 2]
)


cpd_mala_deteccion_periferico = TabularCPD(
    variable='Mala detección perifericos', variable_card=2,
    values=[[0.8, 0.4, 0.6, 0.7, 0.5, 0.4, 0.2, 0.5],
            [0.2, 0.6, 0.4, 0.3, 0.5, 0.6, 0.8, 0.5]],
    evidence=['Periferico', 'SO', 'Motherboard'], evidence_card=[2, 2, 2]
)


# Agregar todos los CPDs al modelo
model.add_cpds(
    cpd_gpu, cpd_cpu, cpd_monitor, cpd_psu, cpd_motherboard, cpd_ram,
    cpd_so, cpd_almacenamiento, cpd_ventiladores, cpd_periferico,
    cpd_pantalla_negra, cpd_no_enciende, cpd_no_deteccion,
    cpd_falta_rendimiento, cpd_pixeles_muertos, cpd_sobreruido, cpd_altas_temperaturas,
    cpd_pantallazo_azul, cpd_inicio_lento, cpd_pitido, cpd_conexion_lenta,
    cpd_mal_funcionamiento_usb, cpd_cuelgues_aleatorios,
    cpd_fallos_guardado, cpd_mala_deteccion_periferico
)


# Exportar el modelo
__all__ = ["model"]
