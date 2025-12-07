# ------------------------------------------------------------------------------
# EJEMPLO DE HERENCIA EN PYTHON
# ------------------------------------------------------------------------------
# La herencia permite crear nuevas clases (hijas) basadas en clases existentes (padres),
# reutilizando y extendiendo su funcionalidad.
# En este ejemplo, crearemos una clase base "Persona" y una clase hija "Estudiante"
# que hereda los atributos y métodos de Persona.
# ------------------------------------------------------------------------------

# Clase base o "padre"
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"👤 Nombre: {self.nombre}, Edad: {self.edad}")

# Clase derivada o "hija" que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamamos al constructor de la clase padre usando super()
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Método propio de la clase hija
    def mostrar_informacion(self):
        # Reutilizamos el método del padre, pero lo extendemos
        super().mostrar_informacion()
        print(f"🎓 Carrera: {self.carrera}")

# ------------------------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Creamos un objeto de la clase base (Persona)
    persona1 = Persona("Laura", 30)
    persona1.mostrar_informacion()

    print("\n---")

    # Creamos un objeto de la clase hija (Estudiante)
    estudiante1 = Estudiante("Mercy Nogales", 21, "Ingeniería en Sistemas")
    estudiante1.mostrar_informacion()

    print("\n✅ Ejemplo de herencia ejecutado correctamente.")
