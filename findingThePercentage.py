if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    # Leemos las notas de los estudiantes y las almacenamos en un diccionario
    for i in range(n):
        line = input().split()
        name = line[0]
        scores = list(map(float, line[1:]))
        student_marks[name] = scores

    # Leemos el nombre del estudiante cuyo promedio queremos calcular
    query_name = input()

    # Calculamos el promedio de las notas del estudiante
    query_scores = student_marks[query_name]
    query_avg = sum(query_scores) / len(query_scores)

    # Imprimimos el promedio con dos decimales
    print("{:.2f}".format(query_avg))
