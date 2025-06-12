#!/usr/bin/env python
'''
Test is even [Python]
Ejemplos de clase
---------------------------
Autor: Prof.Ing.Jesús M.R.González
Version: 1.1

Descripcion:
Programa creado para poner a prueba la función is_even
'''

__author__ = "Prof.Ing.Jesús M.R.González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.1"

import unittest
from number import is_even

class NumbersTestCase(unittest.TestCase):
    """ Ensayo del modulo numbers"""

    def test_is_even(self):
        """ Test si el número 4 es determinado par"""
        number = 4
        self.assertTrue(is_even(number), msg='{} debería haber sido determinado par'.format(number))


if __name__ == '__main__':
    unittest.main()    