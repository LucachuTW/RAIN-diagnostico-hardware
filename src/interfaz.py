from unidecode import unidecode
from problemcauses import list_evidences

def user_interface():
    def normalize(text):
        """Convierte el texto a una forma normalizada sin tildes y en minúsculas."""
        return unidecode(text).lower()

    # Crear un diccionario para mapear las versiones normalizadas a las originales
    normalized_evidences = {normalize(evidence): evidence for evidence in list_evidences}

    def suggest_problem(user_input, evidences):
        """Sugiere problemas similares basándose en la normalización del texto."""
        normalized_input = normalize(user_input)
        return [
            evidences[normalized_key]
            for normalized_key in evidences
            if normalized_input in normalized_key
        ]

    problems = []

    print("\n--- Diagnóstico de Problemas del Ordenador ---")
    print("Ingrese los problemas uno por uno. Escriba 'exit' para finalizar.\n")
    print("Problemas disponibles:")
    print(", ".join([f"'{problem}'" for problem in list_evidences]))
    print("\n")

    while True:
        input_user = input("-> ").strip()  # Limpia espacios en blanco
        normalized_input = normalize(input_user)

        if normalized_input == "exit":
            # Sale del bucle al escribir "exit"
            break
        elif normalized_input in normalized_evidences:
            print("✅ Problema añadido.\n")
            problems.append(normalized_evidences[normalized_input])
        else:
            similar = suggest_problem(input_user, normalized_evidences)
            if similar:
                print(f"❓ Problema no reconocido. Quizás quiso decir: {', '.join(similar)}\n")
            else:
                print("❌ Problema no reconocido. Inténtelo de nuevo.\n")

    if problems:
        print("\n✔️ Diagnóstico completado.")
        print("Problemas detectados:")
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem}")
        return {problem: 1 for problem in problems}
    else:
        print("\n❌ No se han introducido problemas. Finalizando.")
        return {}
