import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

# Definición de la estructura de la red bayesiana
model = BayesianModel([
    ('CPU', 'Falta de rendimiento'),
    ('RAM', 'Falta de rendimiento'),
    ('GPU', 'Falta de rendimiento'),
    ('S.O', 'Falta de rendimiento'),
    ('PSU', 'No enciende'),
    ('Motherboard', 'No enciende'),
    ('GPU', 'Pantalla negra pero ordenador encendido'),
    ('S.O', 'Pantallazo azul'),
    ('RAM', 'Inicio lento'),
    ('Almacenamiento', 'Inicio lento'),
    ('Monitor', 'No envío de señal de algún componente'),
    ('Motherboard', 'No detección o detección parcial de algún componente'),
    ('Ventiladores', 'Temperaturas más altas de lo normal'),
    ('GPU', 'Pixeles muertos'),
    ('GPU', 'Sobreruido de componentes'),
    ('S.O', 'Conexión lenta'),
    ('Almacenamiento', 'Conexión lenta')
])

# Definición de las distribuciones de probabilidad
cpd_cpu = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])
cpd_ram = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])
cpd_gpu = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])
cpd_psu = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])
cpd_motherboard = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])
cpd_so = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])
cpd_al = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])
cpd_v = pd.Series([0.1, 0.9], index=['Faulty', 'Functional'])

# Asumimos que 'Falta de rendimiento' es influenciada por CPU, RAM, GPU, y S.O
cpd_falta_de_rendimiento = pd.DataFrame(data={
    'CPU': ['Functional', 'Functional', 'Functional', 'Functional', 'Faulty', 'Faulty', 'Faulty', 'Faulty'],
    'RAM': ['Functional', 'Functional', 'Faulty', 'Faulty', 'Functional', 'Faulty', 'Faulty', 'Functional'],
    'GPU': ['Functional', 'Faulty', 'Functional', 'Faulty', 'Functional', 'Functional', 'Faulty', 'Faulty'],
    'S.O': ['Functional', 'Functional', 'Functional', 'Faulty', 'Functional', 'Faulty', 'Faulty', 'Faulty'],
    'P(Falta de rendimiento)': [0.05, 0.9, 0.5, 0.95, 0.9, 0.8, 0.7, 0.99]
})

# Añadir las CPDs al modelo
from pgmpy.models import TabularCPD

cpd_falta_de_rendimiento = TabularCPD(variable='Falta de rendimiento', variable_card=2,
    values=[
        [0.05, 0.9, 0.5, 0.95, 0.9, 0.8, 0.7, 0.99],
        [0.95, 0.1, 0.5, 0.05, 0.1, 0.2, 0.3, 0.01]
    ],
    evidence=['CPU', 'RAM', 'GPU', 'S.O'],
    evidence_card=[2, 2, 2, 2]
)

# Ahora agregamos las CPDs al modelo
model.add_cpds(cpd_cpu, cpd_ram, cpd_gpu, cpd_psu, cpd_motherboard, cpd_so, cpd_al, cpd_v, cpd_falta_de_rendimiento)

# Verificamos el modelo
assert model.check_model()

# Inferencia
inference = VariableElimination(model)

# Ejemplo de consulta: calcular la probabilidad de 'Falta de rendimiento' dado que 'CPU' es 'Faulty' y 'RAM' es 'Functional'
query_result = inference.query(variables=['Falta de rendimiento'], evidence={'CPU': 'Faulty', 'RAM': 'Functional'})
print(query_result)
