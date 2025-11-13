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
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self._hours = total_seconds // 3600
        total_seconds %= 3600
        self._minutes = total_seconds // 60
        self._seconds = total_seconds % 60

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @property
    def seconds(self):
        return self._seconds

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"

    def __eq__(self, other):
        if isinstance(other, Duration):
            return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Duration):
            return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Duration):
            total_seconds = (self.hours + other.hours) * 3600 + (self.minutes + other.minutes) * 60 + (self.seconds + other.seconds)
            return Duration(0, 0, total_seconds)
        elif isinstance(other, int):
            total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + other
            return Duration(0, 0, total_seconds)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Duration):
            total_seconds = (self.hours - other.hours) * 3600 + (self.minutes - other.minutes) * 60 + (self.seconds - other.seconds)
            return Duration(0, 0, total_seconds)
        elif isinstance(other, int):
            total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds - other
            return Duration(0, 0, total_seconds)
        return NotImplemented