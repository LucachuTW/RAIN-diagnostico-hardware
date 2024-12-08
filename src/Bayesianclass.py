from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from typing import List


class BayesianHardware:
    def __init__(self, model=None):
        """
        Inicializa la clase con un modelo de red bayesiana.
        :param model: (opcional) Una instancia de BayesianNetwork configurada. Si no se proporciona, se crea una nueva.
        """
        self.model = model if model else BayesianNetwork()
        self.infer = None  # La inferencia se inicializa después de agregar todos los nodos y CPDs
    
    def add_node(self, node):
        """
        Agrega un nodo al modelo.
        :param node: Nombre del nodo.
        """
        self.model.add_node(node)
    
    def add_edge(self, parent, child):
        """
        Agrega una relación (borde) entre dos nodos.
        :param parent: Nodo padre.
        :param child: Nodo hijo.
        """
        self.model.add_edge(parent, child)
    
    def add_cpd(self, cpd):
        """
        Agrega un CPD (Tabla de Probabilidad Condicional) al modelo.
        :param cpd: Instancia de TabularCPD.
        """
        self.model.add_cpds(cpd)

    def add_cpds(self, cpd_list: List[TabularCPD]):
        for cpd in cpd_list:
            self.network.add_cpds(cpd)
    
    def finalize_model(self):
        """
        Verifica y finaliza el modelo, y configura la inferencia.
        """
        assert self.model.check_model(), "El modelo no es consistente. Verifica los nodos y CPDs."
        self.infer = VariableElimination(self.model)
    
    def encontrar_causa_mas_probable(self, evidencias):
        """
        Encuentra la causa más probable de un problema dado un conjunto de evidencias.
        :param evidencias: Diccionario de evidencias donde las claves son variables y los valores son sus estados.
        :return: Tupla (causa_mas_probable, probabilidad), o (None, causas_individuales) si no hay intersección.
        """
        if not self.infer:
            raise ValueError("El modelo no está finalizado. Llama a `finalize_model` primero.")
        
        # Obtener los componentes asociados a todas las evidencias
        componentes_asociados = set(self.model.get_parents(next(iter(evidencias))))
        for problema in evidencias:
            componentes_asociados.intersection_update(self.model.get_parents(problema))
        
        max_prob = 0
        causa_mas_probable = None
        
        # Buscar el componente más probable dentro de los componentes asociados
        for componente in componentes_asociados:
            result = self.infer.query(variables=[componente], evidence=evidencias)
            prob = result.values[1]  # Probabilidad de que el componente esté en estado 1 (fallando)
            
            if prob > max_prob:
                max_prob = prob
                causa_mas_probable = componente

        # Si no hay una causa común más probable, buscar las causas más probables por problema
        if causa_mas_probable is None:
            causas_individuales = []
            for problema in evidencias:
                max_prob_local = 0
                causa_local = None
                for componente in self.model.get_parents(problema):
                    result = self.infer.query(variables=[componente], evidence=evidencias)
                    prob = result.values[1]  # Probabilidad de que el componente esté fallando
                    if prob > max_prob_local:
                        max_prob_local = prob
                        causa_local = componente
                if causa_local is not None:
                    causas_individuales.append((causa_local, max_prob_local))
            
            # Devuelve None como causa principal y las causas individuales como un segundo valor
            return None, causas_individuales
        
        return causa_mas_probable, max_prob


