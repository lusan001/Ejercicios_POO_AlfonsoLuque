# Autor: Alfonso Luque Sánchez
# Ejercicio 2 de POO
"""
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
    Las fracciones pueden operar entre sí.
        Sumar, multiplicar, dividir, restar.
        Ojo!!! esto se puede hacer: f + 1, 5 * f
    Las fracciones se pueden comparar.
        ==, <, <=, >, >=, !=
        Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
        Ojo!!! esto se puede hacer 1 < 1/2
"""

from math import gcd
from symtable import Class

class Fraction:
    def __init__(self, numerador, denominador = 1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        sign = -1 if (numerador * denominador) < 0 else 1
        numerador = abs(numerador)
        denominador = abs(denominador)
        divisor = gcd(numerador, denominador)
        self.__numerador = sign * (numerador // divisor)
        self.__denominador = denominador // divisor

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    def __str__(self):
        return f"{self.__numerador}/{self.__denominador}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerador}, {self.__denominador})"


