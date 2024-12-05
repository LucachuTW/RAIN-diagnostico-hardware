from problemcauses import model
from Bayesianclass import BayesianHardware
from interfaz import user_interface

def validar_evidencias(evidencias, model):
    """
    Valida que las evidencias proporcionadas correspondan a nodos en el modelo.
    """
    if not evidencias:
        print("\n❌ No hay evidencias válidas para diagnosticar.")
        return False

    # Verificar que todas las claves de evidencias estén en los nodos del modelo
    invalid_evidences = [ev for ev in evidencias if ev not in model.nodes]
    if invalid_evidences:
        print(f"\n❌ Las siguientes evidencias no están en el modelo: {', '.join(invalid_evidences)}")
        print("Asegúrate de que los problemas ingresados coincidan con los disponibles.")
        return False

    return True

def main():
    print("\n--- Bienvenido al Diagnóstico de Problemas del Ordenador ---")
    
    # Crear instancia de troubleshooter con el modelo
    troubleshooter = BayesianHardware(model=model)
    troubleshooter.finalize_model()

    # Definir las evidencias ingresadas por el usuario
    evidencias = user_interface()

    if not evidencias:
        print("\n❌ No se han detectado problemas. Saliendo del programa.")
        return

    # Validar evidencias antes de proceder
    if not validar_evidencias(evidencias, troubleshooter.model):
        print("\n❌ Las evidencias no son válidas. Saliendo del programa.")
        return

    # Encontrar la causa más probable
    causa, probabilidad = troubleshooter.encontrar_causa_mas_probable(evidencias)

    # Mostrar los resultados
    print("\n--- Diagnóstico Final ---")
    print(f"La causa más probable de los problemas es: {causa} con una probabilidad de {probabilidad:.2f}")
    print("--- Fin del Diagnóstico ---")

if __name__ == "__main__":
    main()
