#!/usr/bin/env python
'''
Programación orientada a objectos [Python]
Ejemplos de clase
---------------------------
Autor: Prof.Ing.Jesús M.R.González
Version: 1.1

Descripcion:
Modulo con Clase Vehicle y sus derivados
'''

__author__ = "Prof.Ing.Jesús M.R.González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"


class Vehicle():
    '''Clase vehiculo'''
    def __init__(self, model_brand, model_year):
        self.model_brand = model_brand
        self.model_year = model_year


class Wheel():
    '''Clase rueda'''
    def __init__(self):
        self.preassure = 0

    def inflate(self, pressure):
        self.preassure = pressure


class RaceWheel(Wheel):
    '''Clase rueda para carreras'''


class Car(Vehicle):
    '''Clase auto'''
    def __init__(self, model_brand, model_year):
        super().__init__(model_brand, model_year)
        self.wheels = [Wheel() for i in range(4)]


class Truck(Vehicle):
    '''Clase camion'''
    def __init__(self, model_brand, model_year):
        super().__init__(model_brand, model_year)
        self.wheels = [Wheel() for i in range(6)]
