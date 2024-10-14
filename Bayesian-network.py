import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

class BayesianNetworkModel:
    def __init__(self):
        self.model = BayesianNetwork([
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
            ('CPU', 'Sobreruido de componentes'),
            ('S.O', 'Conexión lenta'),
            ('Almacenamiento', 'Conexión lenta')
        ])
        self.define_cpds()
        self.model.add_cpds(*self.cpds)
        assert self.model.check_model(), "El modelo no es válido"

    def define_cpds(self):
        self.cpds = [
            TabularCPD(variable='CPU', variable_card=2, values=[[0.1], [0.9]]),
            TabularCPD(variable='S.O', variable_card=2, values=[[0.7], [0.3]]),
            TabularCPD(variable='PSU', variable_card=2, values=[[0.6], [0.4]]),
            TabularCPD(variable='Motherboard', variable_card=2, values=[[0.5], [0.5]]),
            TabularCPD(variable='GPU', variable_card=2, values=[[0.8], [0.2]]),
            TabularCPD(variable='RAM', variable_card=2, values=[[0.9], [0.1]]),
            TabularCPD(variable='Almacenamiento', variable_card=2, values=[[0.85], [0.15]]),
            TabularCPD(variable='Monitor', variable_card=2, values=[[0.95], [0.05]]),
            TabularCPD(variable='Ventiladores', variable_card=2, values=[[0.75], [0.25]]),
            TabularCPD(variable='Falta de rendimiento', variable_card=2, 
                       values=[[0.9, 0.4], [0.1, 0.6]], 
                       evidence=['S.O'], evidence_card=[2]),
            TabularCPD(variable='No enciende', variable_card=2, 
                       values=[[0.8, 0.3, 0.5, 0.2], [0.2, 0.7, 0.5, 0.8]], 
                       evidence=['PSU', 'Motherboard'], evidence_card=[2, 2]),
            TabularCPD(variable='Pantalla negra pero ordenador encendido', variable_card=2, 
                       values=[[0.7, 0.2], [0.3, 0.8]], 
                       evidence=['GPU'], evidence_card=[2]),
            TabularCPD(variable='Pantallazo azul', variable_card=2, 
                       values=[[0.6, 0.3], [0.4, 0.7]], 
                       evidence=['S.O'], evidence_card=[2]),

        ]

