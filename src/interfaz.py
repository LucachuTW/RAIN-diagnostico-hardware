from problemcauses import list_evidences

def user_interface():
    def suggest_problem(user_input, evidences):
        """Sugiere un problema similar en caso de error."""
        return [evidence for evidence in evidences if user_input.lower() in evidence.lower()]

    problems = []

    print("\n--- Diagnóstico de Problemas del Ordenador ---")
    print("Ingrese los problemas uno por uno. Escriba 'exit' para finalizar.\n")
    print("Problemas disponibles:")
    print(", ".join([f"'{problem}'" for problem in list_evidences]))
    print("\n")

    while True:
        input_user = input("-> ").strip()  # Limpia espacios en blanco

        if input_user.lower() == "exit":
            # Sale del bucle al escribir "exit"
            break
        elif input_user in list_evidences:
            print("✅ Problema añadido.\n")
            problems.append(input_user)
        else:
            similar = suggest_problem(input_user, list_evidences)
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
