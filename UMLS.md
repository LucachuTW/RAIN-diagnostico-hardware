
## UML para el diagrama de componentes

@startuml

'Definimos los componentes principales del sistema

component "Main" as main
component "Módulo Redes Bayesianas" as redesBayesianas
component "Módulo Problemas Hardware" as problemasHardware

' Relacion entre componentes
main --> redesBayesianas : Ejecuta diagnóstico
redesBayesianas --> problemasHardware : Consulta problemas y causas

@enduml

## UML para el diagrama de clase

@startuml
class BayesianNetwork {
  - network: BayesianModel
  + add_node(node: str)
  + add_edge(cause: str, effect: str)
  + add_cpds(cpd_list: List)
  + infer(query: Dict)
}

class HardwareProblem {
  - name: str
  - causes: List[str]
  + get_name(): str
  + add_cause(cause: str)
  + get_causes(): List[str]
}

class Cause {
  - name: str
  - probability: float
  + get_name(): str
  + get_probability(): float
}

class InferenceEngine {
  - model: BayesianNetwork
  + run_inference(query: Dict)
}

BayesianNetwork <|-- HardwareProblem
HardwareProblem <|-- Cause
InferenceEngine --> BayesianNetwork
@enduml


## UML para el diagrama de flujo