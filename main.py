import local
import usuario

def menu():
    while True:
        print("\n=== COMERCONTROL ===")
        print("1. Crear local")
        print("2. Listar locales")
        print("3. Editar local")
        print("4. Eliminar local")
        print("5. Asignar contrato")
        print("6. Registrar arrendatario")
        print("7. Listar arrendatarios")
        print("8. Registrar pago")
        print("9. Consultar historial de pagos")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            local.crear_local()
        elif opcion == "2":
            local.listar_locales()
        elif opcion == "3":
            local.editar_local()
        elif opcion == "4":
            local.eliminar_local()
        elif opcion == "5":
            local.asignar_contrato()
        elif opcion == "6":
            usuario.registrar_arrendatario()
        elif opcion == "7":
            usuario.listar_arrendatarios()
        elif opcion == "8":
            usuario.registrar_pago()
        elif opcion == "9":
            usuario.historial_pagos()
        elif opcion == "10":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
