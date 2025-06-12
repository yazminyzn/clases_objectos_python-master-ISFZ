#!/usr/bin/env python
'''
Programación orientada a objectos [Python]
Ejemplos de clase
---------------------------
Autor: Prof.Ing.Jesús M.R.González
Version: 1.1

Descripcion:
Modulo con Clase Animal y sus derivados
'''

__author__ = "Prof.Ing.Jesús M.R.González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"


class Animal():
    '''Clase base Animal'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        if self.age > 1:
            return 12
        else:
            return 16

    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    '''Clase Dog que hereda de Animal'''
    def sleep(self):
        if self.age > 1:
            return 8
        else:
            return 16

    def speak(self):
        print('Dog say: Guau!')


class Cat(Animal):
    '''Clase Cat que hereda de Animal'''
    def sleep(self):
        if self.age > 1:
            return 10
        else:
            return 18

    def speak(self):
        print('Cat say: Miau!')


class Cow(Animal):
    '''Clase Cow que hereda de Animal'''
    def __init__(self, name, age, cow_type='milk'):
        super().__init__(name, age)
        self.type = cow_type

    def sleep(self):
        if self.age > 3:
            if self.type == 'milk':
                return 10
            else:
                return 4
        else:
            return 10

    def speak(self):
        print('Cow say: Muuu!')
