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

    # Propiedades de solo lectura
    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # Representaciones legibles
    def __str__(self):
        return f"{self.__num}/{self.__den}"

    def __repr__(self):
        return f"Fraction({self.__num}, {self.__den})"

    # Conversión a float (útil para comparar con floats)
    def to_float(self):
        return self.__num / self.__den

    # --- Utilidades internas ---
    def _as_common(self, other):
        """
        Devuelve (a_num, a_den, b_num, b_den) donde la fracción 'other' ha sido
        convertida a (b_num, b_den). Acepta other: Fraction o int.
        """
        if isinstance(other, Fraction):
            return self.__num, self.__den, other.__num, other.__den
        elif isinstance(other, int):
            return self.__num, self.__den, other, 1
        else:
            raise TypeError("Operación solo soporta Fraction o int en esta implementación.")

    # --- Operaciones aritméticas ---
    def __add__(self, other):
        if isinstance(other, Fraction):
            num = self.__num * other.__den + other.__num * self.__den
            den = self.__den * other.__den
        elif isinstance(other, int):
            num = self.__num + other * self.__den
            den = self.__den
        else:
            return NotImplemented
        return Fraction(num, den)

    def __radd__(self, other):
        # soporta int + Fraction
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self.__num * other.__den - other.__num * self.__den
            den = self.__den * other.__den
        elif isinstance(other, int):
            num = self.__num - other * self.__den
            den = self.__den
        else:
            return NotImplemented
        return Fraction(num, den)

    def __rsub__(self, other):
        # other - self  (soportamos other int)
        if isinstance(other, int):
            return Fraction(other, 1) - self
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            num = self.__num * other.__num
            den = self.__den * other.__den
        elif isinstance(other, int):
            num = self.__num * other
            den = self.__den
        else:
            return NotImplemented
        return Fraction(num, den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.__num == 0:
                raise ZeroDivisionError("División por fracción cero.")
            num = self.__num * other.__den
            den = self.__den * other.__num
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("División por cero.")
            num = self.__num
            den = self.__den * other
        else:
            return NotImplemented
        return Fraction(num, den)

    def __rtruediv__(self, other):
        # other / self  (soportamos other int)
        if isinstance(other, int):
            if self.__num == 0:
                raise ZeroDivisionError("División por fracción cero.")
            return Fraction(other * self.__den, self.__num)
        else:
            return NotImplemented

    # --- Comparaciones ---
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.__num * other.__den == other.__num * self.__den
        elif isinstance(other, int):
            return self.__num == other * self.__den
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.__num * other.__den < other.__num * self.__den
        elif isinstance(other, int):
            return self.__num < other * self.__den
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, (Fraction, int)):
            return self == other or self < other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (Fraction, int)):
            return not self <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (Fraction, int)):
            return not self < other
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (Fraction, int)):
            return not self == other
        else:
            return NotImplemented

