from problemcauses import model
from pgmpy.inference import VariableElimination
from Bayesianclass import BayesianHardware

if __name__ == "__main__":
    # Crear instancia de troubleshooter con el modelo
    troubleshooter = BayesianHardware(model=model)
    troubleshooter.finalize_model()

    # Definir las evidencias
    evidencias = {'Mala detección perifericos': 1}

    # Encontrar la causa más probable
    causa, probabilidad = troubleshooter.encontrar_causa_mas_probable(evidencias)

    print(f"\nLa causa más probable de los problemas es: {causa} con una probabilidad de {probabilidad:.2f}")
