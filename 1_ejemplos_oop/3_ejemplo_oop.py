#!/usr/bin/env python
'''
Programación orientada a objectos [Python]
Ejemplos de clase
---------------------------
Autor: Prof.Ing.Jesús M.R.González
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos para contrastar
contra la programamación procedural
'''

__author__ = "Prof.Ing.Jesús M.R.González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"

from animal import Dog, Cat, Cow
import person as p


if __name__ == '__main__':

    animal_1 = Dog('Sirius', 8)
    animal_2 = Cat('Minerva', 1)

    print('¿Cuanto duerme el perro por la noche?', animal_1.sleep())
    print('¿Cuanto duerme el gato por la noche?', animal_2.sleep())

    persona = p.Person('Max')
    print('{} adoptó 2 animales, un perro y un gato'.format(persona.name))

    persona.adopt(animal_1)
    persona.adopt(animal_2)

    print('¿Cómo saludan los animales de', persona.name, '?')

    for animal in persona.animales:
        animal.speak()
