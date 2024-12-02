from problemcauses import model
from pgmpy.inference import VariableElimination
from Bayesianclass import BayesianHardware
from interfaz import user_interface

if __name__ == "__main__":
    # Crear instancia de troubleshooter con el modelo
    troubleshooter = BayesianHardware(model=model)
    troubleshooter.finalize_model()
    print(troubleshooter.model)
    # Definir las evidencias
    
    evidencias = user_interface()

    #evidencias = {'Mala detección perifericos': 1, 'Pantalla negra' : 1}

    # Encontrar la causa más probable
    causa, probabilidad = troubleshooter.encontrar_causa_mas_probable(evidencias)

    print(f"\nLa causa más probable de los problemas es: {causa} con una probabilidad de {probabilidad:.2f}")
