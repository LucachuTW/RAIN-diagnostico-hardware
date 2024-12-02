import PySimpleGUI as sg

def user_interface_with_gui(list_evidences):
    layout = [
        [sg.Text("Introduzca los problemas de su ordenador:")],
        [sg.Combo(list_evidences, key="problem", size=(30, 1), tooltip="Seleccione un problema de la lista")],
        [sg.Button("Añadir problema"), sg.Button("Salir")],
        [sg.Text("Problemas añadidos:", size=(30, 1))],
        [sg.Listbox(values=[], size=(30, 5), key="problems_list")],
    ]

    window = sg.Window("Interfaz de problemas", layout)
    problems = []

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Salir":
            break
        elif event == "Añadir problema":
            input_user = values["problem"]
            if input_user in list_evidences:
                if input_user not in problems:
                    problems.append(input_user)
                    window["problems_list"].update(problems)
                    sg.popup("Problema añadido correctamente.")
                else:
                    sg.popup("Este problema ya está en la lista.")
            else:
                sg.popup("Problema no reconocido, inténtelo de nuevo.")

    window.close()

    if problems:
        sg.popup("RESUELTO")
        return {problem: 1 for problem in problems}
    else:
        sg.popup("No se han introducido problemas")
        return "No se han introducido problemas"

# Ejemplo de uso

list_evidences = ["Pantalla azul", "No arranca", "Se reinicia solo", "No funciona internet"]
result = user_interface_with_gui(list_evidences)
print(result)
