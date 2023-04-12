if __name__ == '__main__':
    n = int(input())
    scores = []

    for i in range(n):
        name = input()
        score = float(input())
        scores.append([name, score])

    # Ordenamos la lista de puntuaciones de manera ascendente
    scores_sorted = sorted(scores, key=lambda x: x[1])

    # Buscamos la segunda puntuación más baja
    second_lowest_score = None
    for i in range(n):
        if scores_sorted[i][1] > scores_sorted[0][1]:
            second_lowest_score = scores_sorted[i][1]
            break

    # Imprimimos los nombres de los estudiantes con la segunda puntuación más baja
    second_lowest_names = []
    for i in range(n):
        if scores[i][1] == second_lowest_score:
            second_lowest_names.append(scores[i][0])

    # Ordenamos los nombres de los estudiantes de manera alfabética y los imprimimos
    second_lowest_names_sorted = sorted(second_lowest_names)
    for name in second_lowest_names_sorted:
        print(name)
