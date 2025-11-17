# Autor: Alfonso Luque Sánchez
# Ejercicio 2 de POO
"""
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
    Las fracciones pueden operar entre sí.
        Sumar, multiplicar, dividir, restar.
        ¡Ojo!!! Esto se puede hacer: f + 1, 5 * f
    Las fracciones se pueden comparar.
        ¡==, <, <=, >, >=, !=
        Ojo!!! ¡Estas dos fracciones son iguales: 1/2 y 2/4
        Ojo!!! Esto se puede hacer 1 < 1/2
"""

from math import gcd

class Fraction:
    """
    Clase que representa fracciones (numerador / denominador).
    - Se simplifican automáticamente.
    - No se permite denominador 0.
    - Soporta operaciones con otras Fraction y con enteros (int).
    - Soporta comparaciones con otras Fraction y con enteros.
    """

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("El denominador no puede ser 0.")
        # Normalizar signo: el denominador siempre será positivo
        sign = -1 if numerator * denominator < 0 else 1
        n, d = abs(numerator), abs(denominator)
        common = gcd(n, d)
        # Guardamos la fracción ya simplificada
        self.__num = sign * (n // common)
        self.__den = d // common

