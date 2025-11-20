import local
import usuario


def menu_locales():
    while True:
        print("\n=== GESTIÓN DE LOCALES ===")
        print("1. Crear local")
        print("2. Listar locales")
        print("3. Buscar local")
        print("4. Editar local")
        print("5. Eliminar local")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            local.crear_local()
        elif opcion == "2":
            local.listar_locales()
        elif opcion == "3":
            local.buscar_local()
        elif opcion == "4":
            local.editar_local()
        elif opcion == "5":
            local.eliminar_local()
        elif opcion == "0":
            break
        else:
            print(" Opción inválida.")



def menu_arrendatarios():
    while True:
        print("\n=== GESTIÓN DE ARRENDATARIOS ===")
        print("1. Registrar arrendatario")
        print("2. Listar arrendatarios")
        print("3. Buscar arrendatario")
        print("4. Editar arrendatario")      
        print("5. Eliminar arrendatario")    
        print("6. Asignar contrato")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario.registrar_arrendatario()
        elif opcion == "2":
            usuario.listar_arrendatarios()
        elif opcion == "3":
            usuario.buscar_arrendatario()
        elif opcion == "4":
            usuario.editar_arrendatario()   
        elif opcion == "5":
            usuario.eliminar_arrendatario() 
        elif opcion == "6":
            local.asignar_contrato()
        elif opcion == "0":
            break
        else:
            print(" Opción inválida.")


def menu_pagos():
    while True:
        print("\n=== GESTIÓN DE PAGOS ===")
        print("1. Registrar pago")
        print("2. Consultar historial")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario.registrar_pago()
        elif opcion == "2":
            usuario.historial_pagos()
        elif opcion == "0":
            break
        else:
            print(" Opción inválida.")



def menu_principal():
    while True:
        print("\n=== COMERCONTROL ===")
        print("(L) Locales")
        print("(A) Arrendatarios")
        print("(P) Pagos")
        print("(S) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion.upper() == "L":
            menu_locales()
        elif opcion.upper() == "A":
            menu_arrendatarios()
        elif opcion.upper() == "P":
            menu_pagos()
        elif opcion.upper() == "S":
            print("Cerrando sistema...")
            break
        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    menu_principal()
