if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Usamos una lista de comprensión para generar todas las posibles combinaciones
    # de i, j, k tales que i+j+k != n y i <= x, j <= y, k <= z
    lista = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

    # Imprimimos la lista resultante
    print(lista)
