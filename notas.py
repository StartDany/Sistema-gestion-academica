def agregar_nota(estudiante, nota):
    if 0 <= nota <= 5:
        estudiante["notas"].append(nota)
        return True
    return False


def calcular_promedio(estudiante):
    notas = estudiante["notas"]
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def estado_estudiante(estudiante):
    promedio = calcular_promedio(estudiante)
    if promedio >= 3:
        return "APROBADO"
    return "NO APROBADO"
