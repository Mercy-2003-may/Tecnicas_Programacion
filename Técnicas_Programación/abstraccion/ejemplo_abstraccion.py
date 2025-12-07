# ------------------------------------------------------------
# EJEMPLO DE ABSTRACCIÓN EN PYTHON
# ------------------------------------------------------------
# La abstracción consiste en centrarse en los aspectos esenciales
# de un objeto y ocultar los detalles innecesarios.
# En este ejemplo, definimos una clase base "MaterialBiblioteca"
# que representa lo común a todos los materiales de una biblioteca.
# Luego, las clases "Libro" y "Revista" heredan de ella
# y solo añaden los detalles relevantes de cada tipo.
# ------------------------------------------------------------

# Importamos las herramientas necesarias para crear clases abstractas
from abc import ABC, abstractmethod


# ------------------------------------------------------------
# Clase abstracta (no se puede instanciar directamente)
# ------------------------------------------------------------
# Esta clase define los atributos comunes a todos los materiales
# (título, autor y año), pero deja que las subclases definan
# su propio comportamiento en el método mostrar_informacion().
class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    @abstractmethod
    def mostrar_informacion(self):
        pass  # Se deja sin implementar porque cada subclase lo personaliza


# ------------------------------------------------------------
# Clase concreta que representa un libro
# ------------------------------------------------------------
# Hereda de MaterialBiblioteca e implementa el método abstracto.
# Además, agrega un nuevo atributo: género.
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self.genero = genero

    def mostrar_informacion(self):
        print(f"[LIBRO] '{self.titulo}' de {self.autor} ({self.anio}) - Género: {self.genero}")


# ------------------------------------------------------------
# Clase concreta que representa una revista
# ------------------------------------------------------------
# También hereda de MaterialBiblioteca e implementa el método abstracto.
# Agrega un nuevo atributo: edición.
class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, anio, edicion):
        super().__init__(titulo, autor, anio)
        self.edicion = edicion

    def mostrar_informacion(self):
        print(f"[REVISTA] '{self.titulo}' - Edición {self.edicion} ({self.anio})")


# ------------------------------------------------------------
# Uso de las clases (programa principal)
# ------------------------------------------------------------
# Aquí creamos objetos de tipo Libro y Revista,
# y los almacenamos en una lista para recorrerlos e imprimir su información.
if __name__ == "__main__":
    materiales = [
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico"),
        Revista("National Geographic", "Varios autores", 2023, "Marzo")
    ]

    for material in materiales:
        material.mostrar_informacion()

    print("\n✅ Ejemplo de abstracción ejecutado correctamente.")
