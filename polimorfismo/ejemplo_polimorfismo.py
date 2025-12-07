# --------------------------------------------------------------
# EJEMPLO DE POLIMORFISMO EN PYTHON
# --------------------------------------------------------------
# El polimorfismo permite usar un mismo método en diferentes clases,
# haciendo que cada clase lo implemente de forma distinta según su contexto.
# En este ejemplo, mostramos cómo diferentes tipos de figuras pueden
# calcular su área utilizando el mismo método "calcular_area()".
# --------------------------------------------------------------

import math

# Clase base
class Figura:
    def calcular_area(self):
        # Método general que será sobreescrito por las clases hijas
        pass

# Clases derivadas
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# --------------------------------------------------------------
# Uso del polimorfismo
# --------------------------------------------------------------
# Aquí creamos una lista de figuras diferentes, pero todas comparten
# el mismo método calcular_area(), que se comporta según su clase.

if __name__ == "__main__":
    figuras = [
        Cuadrado(5),
        Circulo(3),
        Triangulo(4, 6)
    ]

    for figura in figuras:
        print(f"Área de {figura.__class__.__name__}: {figura.calcular_area():.2f}")

    print("\n✅ Ejemplo de polimorfismo ejecutado correctamente.")
