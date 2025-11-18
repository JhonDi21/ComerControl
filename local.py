# ============================================
#               local.py
# ============================================

import json
import os
from datetime import datetime

DATA_FILE = "data.json"

# ==========================
#  Funciones base
# ==========================

def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return {"locales": [], "arrendatarios": [], "contratos": [], "pagos": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ==========================
# Función para evitar campos vacíos
# ==========================

def pedir_input(mensaje):
    valor = ""
    while not valor.strip():
        valor = input(mensaje).strip()
        if not valor:
            print("❌ Este campo no puede estar vacío.")
    return valor

# ==========================
# Función para validar fechas YYYY-MM-DD
# ==========================

def pedir_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("❌ Fecha inválida. Use formato YYYY-MM-DD (ej: 2026-12-05).")

# ==========================
# Gestión de Locales
# ==========================

def crear_local():
    data = cargar_datos()

    numero = pedir_input("Número del local: ")
    tamaño = pedir_input("Tamaño (m²): ")
    ubicacion = pedir_input("Ubicación: ")
    estado = "Disponible"

    nuevo_local = {
        "numero": numero,
        "tamaño": tamaño,
        "ubicacion": ubicacion,
        "estado": estado
    }

    data["locales"].append(nuevo_local)
    guardar_datos(data)
    print("✔ Local creado con éxito.")

def listar_locales():
    data = cargar_datos()
    contratos = data["contratos"]
    arrendatarios = data["arrendatarios"]

    if not data["locales"]:
        print("No hay locales registrados.")
        return

    print("\n=== LISTA DE LOCALES ===")
    for local in data["locales"]:
        estado = local["estado"]
        info_extra = ""

        if estado == "Ocupado":
            contrato = next((c for c in contratos if c["local"] == local["numero"]), None)
            if contrato:
                arr = next((a for a in arrendatarios if a["cedula"] == contrato["arrendatario"]), None)
                if arr:
                    info_extra = f" - Ocupado por: {arr['nombre']} (CC: {arr['cedula']})"

        print(f"Local {local['numero']} - {local['ubicacion']} - {estado}{info_extra}")

def editar_local():
    data = cargar_datos()
    numero = pedir_input("Número del local a editar: ")

    local = next((l for l in data["locales"] if l["numero"] == numero), None)
    if not local:
        print("❌ Local no encontrado.")
        return

    nuevo_tamaño = input(f"Nuevo tamaño ({local['tamaño']}): ").strip()
    nueva_ubicacion = input(f"Nueva ubicación ({local['ubicacion']}): ").strip()

    if nuevo_tamaño:
        local["tamaño"] = nuevo_tamaño
    if nueva_ubicacion:
        local["ubicacion"] = nueva_ubicacion

    guardar_datos(data)
    print("✔ Local actualizado correctamente.")

def eliminar_local():
    data = cargar_datos()
    numero = pedir_input("Número del local a eliminar: ")

    data["locales"] = [l for l in data["locales"] if l["numero"] != numero]
    guardar_datos(data)
    print("✔ Local eliminado correctamente.")

# ==========================
# Gestión de Contratos
# ==========================

def asignar_contrato():
    data = cargar_datos()

    cedula = pedir_input("Cédula del arrendatario: ")
    local_num = pedir_input("Número del local a arrendar: ")

    arr = next((a for a in data["arrendatarios"] if a["cedula"] == cedula), None)
    loc = next((l for l in data["locales"] if l["numero"] == local_num), None)

    if not arr:
        print("❌ Arrendatario no encontrado.")
        return
    if not loc:
        print("❌ Local no encontrado.")
        return
    if loc["estado"] == "Ocupado":
        print("❌ El local ya está ocupado.")
        return

    inicio = pedir_fecha("Fecha de inicio (YYYY-MM-DD): ")
    fin = pedir_fecha("Fecha de fin (YYYY-MM-DD): ")

    contrato = {
        "arrendatario": cedula,
        "local": local_num,
        "inicio": inicio,
        "fin": fin
    }

    data["contratos"].append(contrato)
    loc["estado"] = "Ocupado"

    guardar_datos(data)
    print("✔ Contrato asignado correctamente.")
