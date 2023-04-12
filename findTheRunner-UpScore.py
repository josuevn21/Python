if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Convertimos el objeto "map" en una lista y la ordenamos de manera descendente
    arr_desc = sorted(list(arr), reverse=True)

    # Buscamos el segundo elemento más grande de la lista ordenada
    second_largest = None
    for num in arr_desc:
        if num < arr_desc[0]:
            second_largest = num
            break

    # Imprimimos el segundo elemento más grande o "None" si no existe
    print(second_largest)
