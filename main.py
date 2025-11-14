import local
import usuario

def menu_locales():
    while True:
        print("\n=== GESTIÓN DE LOCALES ===")
        print("1. Crear local")
        print("2. Listar locales")
        print("3. Editar local")
        print("4. Eliminar local")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            local.crear_local()
        elif opcion == "2":
            local.listar_locales()
        elif opcion == "3":
            local.editar_local()
        elif opcion == "4":
            local.eliminar_local()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_arrendatarios():
    while True:
        print("\n=== GESTIÓN DE ARRENDATARIOS ===")
        print("1. Asignar contrato")
        print("2. Registrar arrendatario")
        print("3. Listar arrendatarios")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            local.asignar_contrato()
        elif opcion == "2":
            usuario.registrar_arrendatario()
        elif opcion == "3":
            usuario.listar_arrendatarios()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_pagos():
    while True:
        print("\n=== GESTIÓN DE PAGOS ===")
        print("1. Registrar pago")
        print("2. Consultar historial de pagos")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            usuario.registrar_pago()
        elif opcion == "2":
            usuario.historial_pagos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_principal():
    while True:
        print("\n=== COMERCONTROL ===")
        print("(L) Gestionar Locales")
        print("(A) Gestionar Arrendatarios")
        print("(P) Gestionar Pagos")
        print("(S) Salir")

        opcion = input("Seleccione una opción: ")
        if opcion.upper() == "L":
            menu_locales()
        elif opcion.upper() == "A":
            menu_arrendatarios()
        elif opcion.upper() == "P":
            menu_pagos()
        elif opcion.upper() == "S":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
