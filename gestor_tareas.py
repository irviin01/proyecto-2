import json
from pathlib import Path

ARCHIVO = Path("tareas.json")


def cargar_tareas():
    if ARCHIVO.exists():
        try:
            return json.loads(ARCHIVO.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def guardar_tareas(tareas):
    ARCHIVO.write_text(
        json.dumps(tareas, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def mostrar_tareas(tareas):
    print("\n--- MIS TAREAS ---")
    if not tareas:
        print("No hay tareas registradas.")
        return

    for i, tarea in enumerate(tareas, start=1):
        estado = "✓" if tarea["completada"] else " "
        print(f"{i}. [{estado}] {tarea['titulo']}")


def agregar_tarea(tareas):
    titulo = input("Escribe la nueva tarea: ").strip()
    if titulo:
        tareas.append({"titulo": titulo, "completada": False})
        guardar_tareas(tareas)
        print("Tarea agregada correctamente.")
    else:
        print("La tarea no puede estar vacía.")


def completar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return

    try:
        numero = int(input("Número de tarea a completar: "))
        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            guardar_tareas(tareas)
            print("Tarea completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debes escribir un número.")


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return

    try:
        numero = int(input("Número de tarea a eliminar: "))
        if 1 <= numero <= len(tareas):
            eliminada = tareas.pop(numero - 1)
            guardar_tareas(tareas)
            print(f"Se eliminó: {eliminada['titulo']}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debes escribir un número.")


def menu():
    tareas = cargar_tareas()

    while True:
        print("\n=== GESTOR DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
