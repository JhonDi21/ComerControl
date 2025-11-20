from local import cargar_datos, guardar_datos, pedir_input

def registrar_arrendatario():
    data = cargar_datos()

    nombre = pedir_input("Nombre del arrendatario: ")
    cedula = pedir_input("Cédula: ")
    telefono = pedir_input("Teléfono: ")

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

        locales_arrendados = [
            contrato["local"]
            for contrato in data["contratos"]
            if contrato["arrendatario"] == a["cedula"]
        ]

        locales_txt = ", ".join(locales_arrendados) if locales_arrendados else "Ninguno"

        print(
            f"{a['nombre']} - Cédula: {a['cedula']} - Tel: {a['telefono']} - Locales arrendados: {locales_txt}"
        )
        
def buscar_arrendatario():
    data = cargar_datos()
    cedula = pedir_input("Ingrese la cédula del arrendatario: ")

    arr = next((a for a in data["arrendatarios"] if a["cedula"] == cedula), None)

    if not arr:
        print(" No existe un arrendatario con esa cédula.")
        return

    print("\n=== INFORMACIÓN DEL ARRENDATARIO ===")
    print(f"Nombre: {arr['nombre']}")
    print(f"Cédula: {arr['cedula']}")
    print(f"Teléfono: {arr['telefono']}")

    # Mostrar los locales arrendados
    contratos = data["contratos"]
    locales_arr = [c["local"] for c in contratos if c["arrendatario"] == cedula]

    if locales_arr:
        print(f"Locales arrendados: {', '.join(locales_arr)}")
    else:
        print("Locales arrendados: Ninguno")

    # Mostrar locales disponibles
    disponibles = [l["numero"] for l in data["locales"] if l["estado"] == "Disponible"]

    print(f"Locales disponibles: {', '.join(disponibles) if disponibles else 'Ninguno'}")



def editar_arrendatario():
    data = cargar_datos()
    cedula = pedir_input("Cédula del arrendatario a editar: ")

    arr = next((a for a in data["arrendatarios"] if a["cedula"] == cedula), None)

    if not arr:
        print(" Arrendatario no encontrado.")
        return

    print("\nDeje vacío si NO desea modificar un campo.\n")

    nuevo_nombre = input(f"Nuevo nombre ({arr['nombre']}): ").strip()
    nuevo_telefono = input(f"Nuevo teléfono ({arr['telefono']}): ").strip()
    nueva_cedula = input(f"Nueva cédula ({arr['cedula']}): ").strip()

    if nuevo_nombre:
        arr["nombre"] = nuevo_nombre
    if nuevo_telefono:
        arr["telefono"] = nuevo_telefono
    if nueva_cedula:
        # Actualizar contratos si cambia la cédula
        for c in data["contratos"]:
            if c["arrendatario"] == cedula:
                c["arrendatario"] = nueva_cedula
        arr["cedula"] = nueva_cedula

    guardar_datos(data)
    print(" Arrendatario actualizado correctamente.")

def eliminar_arrendatario():
    data = cargar_datos()
    cedula = pedir_input("Cédula del arrendatario a eliminar: ")

    arr = next((a for a in data["arrendatarios"] if a["cedula"] == cedula), None)

    if not arr:
        print(" No existe un arrendatario con esa cédula.")
        return

    # Liberar locales y borrar contratos
    nuevos_contratos = []
    for contrato in data["contratos"]:
        if contrato["arrendatario"] == cedula:
            # liberar local
            for l in data["locales"]:
                if l["numero"] == contrato["local"]:
                    l["estado"] = "Disponible"
        else:
            nuevos_contratos.append(contrato)

    data["contratos"] = nuevos_contratos

    # Eliminar arrendatario
    data["arrendatarios"] = [a for a in data["arrendatarios"] if a["cedula"] != cedula]

    guardar_datos(data)
    print(" Arrendatario eliminado correctamente.")


def registrar_pago():
    data = cargar_datos()

    local_num = pedir_input("Número del local: ")
    fecha = pedir_input("Fecha del pago (YYYY-MM-DD): ")
    monto_input = pedir_input("Monto pagado: ")

    try:
        monto = float(monto_input)
    except ValueError:
        print(" El monto debe ser un número.")
        return

    pago = {"local": local_num, "fecha": fecha, "monto": monto}

    data["pagos"].append(pago)
    guardar_datos(data)
    print(" Pago registrado correctamente.")


def historial_pagos():
    data = cargar_datos()

    local_num = pedir_input("Número del local: ")
    pagos_local = [p for p in data["pagos"] if p["local"] == local_num]

    if not pagos_local:
        print("No hay pagos registrados para ese local.")
        return

    print(f"\n=== HISTORIAL DE PAGOS - LOCAL {local_num} ===")
    for p in pagos_local:
        print(f"Fecha: {p['fecha']} | Monto: ${p['monto']}")
