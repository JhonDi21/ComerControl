#PRUEBA JHON PEREZ
import json
import os

DATA_FILE = "data.json"

def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return {"locales": [], "arrendatarios": [], "contratos": [], "pagos": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ---------- Gestión de Locales ----------
def crear_local():
    data = cargar_datos()
    numero = input("Número del local: ")
    tamaño = input("Tamaño (m²): ")
    ubicacion = input("Ubicación: ")
    estado = "Disponible"

    nuevo_local = {
        "numero": numero,
        "tamaño": tamaño,
        "ubicacion": ubicacion,
        "estado": estado
    }
    data["locales"].append(nuevo_local)
    guardar_datos(data)
    print(" Local creado con éxito.")

def listar_locales():
    data = cargar_datos()
    if not data["locales"]:
        print("No hay locales registrados.")
        return
    print("\n=== LISTA DE LOCALES ===")
    for local in data["locales"]:
        print(f"Local {local['numero']} - {local['ubicacion']} - {local['estado']}")

def editar_local():
    data = cargar_datos()
    numero = input("Número del local a editar: ")
    local = next((l for l in data["locales"] if l["numero"] == numero), None)
    if not local:
        print(" Local no encontrado.")
        return
    local["tamaño"] = input(f"Nuevo tamaño ({local['tamaño']}): ") or local["tamaño"]
    local["ubicacion"] = input(f"Nueva ubicación ({local['ubicacion']}): ") or local["ubicacion"]
    guardar_datos(data)
    print(" Local actualizado correctamente.")

def eliminar_local():
    data = cargar_datos()
    numero = input("Número del local a eliminar: ")
    data["locales"] = [l for l in data["locales"] if l["numero"] != numero]
    guardar_datos(data)
    print(" Local eliminado correctamente.")

# ---------- Gestión de Contratos ----------
def asignar_contrato():
    data = cargar_datos()
    cedula = input("Cédula del arrendatario: ")
    local_num = input("Número del local a arrendar: ")

    arr = next((a for a in data["arrendatarios"] if a["cedula"] == cedula), None)
    loc = next((l for l in data["locales"] if l["numero"] == local_num), None)

    if not arr or not loc:
        print(" Arrendatario o local no encontrado.")
        return
    if loc["estado"] == "Ocupado":
        print(" El local ya está ocupado.")
        return

    inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fin = input("Fecha de fin (YYYY-MM-DD): ")

    contrato = {
        "arrendatario": cedula,
        "local": local_num,
        "inicio": inicio,
        "fin": fin
    }
    data["contratos"].append(contrato)
    loc["estado"] = "Ocupado"
    guardar_datos(data)
    print(" Contrato asignado correctamente.")
