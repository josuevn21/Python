if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # Convertimos la lista de enteros en una tupla
    tuple_list = tuple(integer_list)

    # Imprimimos el hash de la tupla
    print(hash(tuple_list))
