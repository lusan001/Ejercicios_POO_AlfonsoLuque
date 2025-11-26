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
        ¡==, <, <=, >, >=,!=
        Ojo!!! ¡Estas dos fracciones son iguales: 1/2 y 2/4
        Ojo!!! Esto se puede hacer 1 < 1/2
"""

from math import gcd

class Fraction:
    """
    Clase que representa fracciones (numerador / denominador).
    - Se simplifican automáticamente.
    - No se permite denominador 0.
    - Soporta suma con Fraction y con int (incluye int + Fraction).
    """

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("El denominador no puede ser 0.")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Simplificar la fracción
        g = gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator +
                             other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            new_numerator = self.numerator + other * self.denominator
            new_denominator = self.denominator
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator -
                             other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            new_numerator = self.numerator - other * self.denominator
            new_denominator = self.denominator
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)

    def __rsub__(self, other):
        if isinstance(other, int):
            new_numerator = other * self.denominator - self.numerator
            new_denominator = self.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            new_numerator = self.numerator * other
            new_denominator = self.denominator
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        elif isinstance(other, int):
            new_numerator = self.numerator
            new_denominator = self.denominator * other
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)
    def __rtruediv__(self, other):
        if isinstance(other, int):
            new_numerator = other * self.denominator
            new_denominator = self.numerator
            return Fraction(new_numerator, new_denominator)
        else:
            return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator and
                    self.denominator == other.denominator)
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        else:
            return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator <
                    other.numerator * self.denominator)
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            return NotImplemented
    def __le__(self, other):
        return self < other or self == other
    def __gt__(self, other):
        return not (self <= other)
    def __ge__(self, other):
        return not (self < other)
    def __ne__(self, other):
        return not (self == other)

