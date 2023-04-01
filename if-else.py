# # Pedimos el número entero al usuario
# n = int(input())

# # Verificamos si es par o impar
# if n % 2 == 1: # Si el residuo de n/2 es 1, es impar
#     print("Weird")
# else:
#     if n >= 2 and n <= 5: # Si es par y está en el rango [2,5], es Not Weird
#         print("Not Weird")
#     elif n >= 6 and n <= 20: # Si es par y está en el rango [6,20], es Weird
#         print("Weird")
#     else: # Si es par y es mayor que 20, es Not Weird
#         print("Not Weird")

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1: # Si el residuo de n/2 es 1, es impar
        print("Weird")
    else:
        if n >= 2 and n <= 5: # Si es par y está en el rango [2,5], es Not Weird
            print("Not Weird")
        elif n >= 6 and n <= 20: # Si es par y está en el rango [6,20], es Weird
            print("Weird")
        else: # Si es par y es mayor que 20, es Not Weird
            print("Not Weird")
