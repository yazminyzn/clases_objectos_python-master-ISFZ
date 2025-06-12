#!/usr/bin/env python
'''
Numbers - Unit test [Python]
Ejemplos de clase
---------------------------
Autor: Prof.Ing.Jesús M.R.González
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de como realizar unit test
'''

__author__ = "Prof.Ing.Jesús M.R.González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"


def is_even(number):
    """Retorna True si el número es par"""

    if (number / 2) == 0:   # Adrede se deja por error el símbolo "/" en vez de "%"
        return True     # Número par
    else:
        return False    # Número impar


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    number = 4
    print('El número',number,'es par:',is_even(number))