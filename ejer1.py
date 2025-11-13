# Autor: Alfonso Luque Sánchez
# Ejercicio 1 de POO
"""
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

Crear duraciones de tiempos.
    Ejemplo: t = Duration(10,20,56)
    Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
    Si no indico la hora, minuto o segundo estos valores son cero:
        Duration() --> (0, 0, 0)
        Duration(34) --> (34, 0, 0)
        Duration(34, 15) --> (34, 15, 0)
        Duration(34, 61) --> (35, 1, 0)
        Las duraciones de tiempo se pueden comparar.
        A las duraciones de tiempo les puedo sumar y restar segundos.
        Las duraciones de tiempo se pueden sumar y restar.
"""


class Duration:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
        self.__normalize()

    def __normalize(self):
        """
        Cambia las horas, minutos y segundos del objeto Duration para que estén en el rango de valores adecuados.
        Pasamos todo a segundos, recalculamos las horas, minutos y segundos.
        No admitimos duraciones de tiempo negativas, lanzamos excepción en ese caso.
        """
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60

    def __total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def __str__(self):
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__hours}, {self.__minutes}, {self.__seconds})"

    # Sobrecarga de operadores

    def __add__(self, other):
        if isinstance(other, Duration):
            return Duration(self.__hours + other.__hours, self.__minutes + other.__minutes,
                            self.__seconds + other.__seconds)
        else:
            return Duration(self.__hours, self.__minutes, self.__seconds + other)

    def __sub__(self, other):
        if isinstance(other, Duration):
            return Duration(self.__hours - other.__hours, self.__minutes - other.__minutes,
                            self.__seconds - other.__seconds)
        else:
            return Duration(self.__hours, self.__minutes, self.__seconds - other)

    def __eq__(self, other):
        return (self.__hours, self.__minutes, self.__seconds) == (other.__hours, other.__minutes, other.__seconds)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.__total_seconds() < other.__total_seconds()

    def __le__(self, other):
        return self.__total_seconds() <= other.__total_seconds()

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
