from notas import (calcular_promedio)

estudiantes = []

def agregar_estudiante(codigo, nombre):
    estudiante = {
        "codigo": codigo,
        "nombre": nombre,
        "notas": []
    }
    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            print("Error: Ya existe un estudiante con ese código.")
            return
    estudiantes.append(estudiante)

def mostrar_estudiantes():
    if not estudiantes:
        print("No existen estudiantes registrados.")
        return

    for estudiante in estudiantes:
        print(estudiante["codigo"], "-", estudiante["nombre"])

def buscar_estudiante(codigo):
    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            return estudiante
    return None

def eliminar_estudiante(codigo):
    estudiante = buscar_estudiante(codigo)
    if estudiante:
        estudiantes.remove(estudiante)
        return True
    return False

def mejor_estudiante(estudiantes):
    if not estudiantes:
        return None

    mejor = estudiantes[0]

    for estudiante in estudiantes:
        if calcular_promedio(estudiante) > calcular_promedio(mejor):
            mejor = estudiante

    return mejor

