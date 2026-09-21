from estudiante import (agregar_estudiante,mostrar_estudiantes,buscar_estudiante,eliminar_estudiante)

from notas import (agregar_nota,calcular_promedio,estado_estudiante)

def menu():
    while True:
        print("====================================")
        print("   SISTEMA DE GESTION ACADEMICA")
        print("====================================")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Buscar estudiante")
        print("5. Registrar nota")
        print("6. Consultar promedio")
        print("7. Salir")
        opcion=input("Seleccione que quiere hacer(1-7): ")
        if opcion == "1":   
            codigo=input("Ingrese el codigo del estudiante: ")
            nombre=input("Ingrese el nombre del estudiante: ")
            agregar_estudiante(codigo, nombre)
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            codigo_delete=input("Ingrese el codigo del estudiante a eliminar: ")
            if eliminar_estudiante(codigo_delete):
                print("Estudiante eliminado exitosamente.")
            else:
                print("No se encontro ningun estudiante con ese codigo.")
        elif opcion == "4":
            codigo_search=input("Ingrese el codigo del estudiante a buscar: ")
            estudiante = buscar_estudiante(codigo_search)
            if estudiante:
                print("Estudiante encontrado:", estudiante)
            else:
                print("No se encontro ninguno estudiante con ese codigo.")
        elif opcion == "5":
            codigo_search=input("Ingrese el codigo del estudiante para agregar nota: ")
            estudiante = buscar_estudiante(codigo_search)
            if estudiante:
                try:    
                    nota = float(input("Digite la nota: "))
                    if agregar_nota(estudiante, nota):
                        print("Nota agregada exitosamente.")
                    else:
                        print("La nota debe estar entre 0 y 5.")
                except ValueError:
                    print("Error: debe ingresar un numero.")
            else:
                print("No se encontro ningun estudiante con ese codigo.")
        elif opcion == "6":
            codigo_search=input("Ingrese el codigo del estudiante para calcular promedio: ")
            estudiante = buscar_estudiante(codigo_search)  
            if estudiante:
                promedio = calcular_promedio(estudiante)
                if promedio > 0:
                    print(f"Promedio del estudiante {estudiante['nombre']}: {promedio:.2f}") 
                else:
                    print("El estudiante no tiene notas registradas.")
            else:
                print("No se encontro ningun estudiante con ese codigo.")    
        elif opcion == "7":
            print("Hasta luego")
            break 
        else:
            print("Opcion no valida, intente de nuevo.")

menu()