from local import cargar_datos, guardar_datos

# ---------- Arrendatarios ----------
def registrar_arrendatario():
    data = cargar_datos()
    nombre = input("Nombre del arrendatario: ")
    cedula = input("Cédula: ")
    telefono = input("Teléfono: ")

    arr = {"nombre": nombre, "cedula": cedula, "telefono": telefono}
    data["arrendatarios"].append(arr)
    guardar_datos(data)
    print(" Arrendatario registrado correctamente.")

def listar_arrendatarios():
    data = cargar_datos()
    if not data["arrendatarios"]:
        print("No hay arrendatarios registrados.")
        return
    print("\n=== LISTA DE ARRENDATARIOS ===")
    for a in data["arrendatarios"]:
        print(f"{a['nombre']} - Cédula: {a['cedula']} - Tel: {a['telefono']}")

# ---------- Pagos ----------
def registrar_pago():
    data = cargar_datos()
    local_num = input("Número del local: ")
    fecha = input("Fecha del pago (YYYY-MM-DD): ")
    monto = float(input("Monto pagado: "))

    pago = {"local": local_num, "fecha": fecha, "monto": monto}
    data["pagos"].append(pago)
    guardar_datos(data)
    print(" Pago registrado correctamente.")

def historial_pagos():
    data = cargar_datos()
    local_num = input("Número del local: ")
    pagos_local = [p for p in data["pagos"] if p["local"] == local_num]

    if not pagos_local:
        print("No hay pagos registrados para ese local.")
        return
    print(f"\n=== HISTORIAL DE PAGOS - LOCAL {local_num} ===")
    for p in pagos_local:
        print(f"Fecha: {p['fecha']} | Monto: ${p['monto']}")
