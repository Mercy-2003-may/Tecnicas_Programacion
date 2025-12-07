# ------------------------------------------------------------------------------
# EJEMPLO DE ENCAPSULACIÓN EN PYTHON
# ------------------------------------------------------------------------------
# La encapsulación permite ocultar los datos internos de un objeto
# y controlar cómo se accede o modifica dicha información.
# En este ejemplo, definimos una clase "CuentaBancaria" que protege
# el saldo mediante atributos privados y métodos para depositar y retirar dinero.
# ------------------------------------------------------------------------------

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # Atributos privados (no deben accederse directamente desde fuera de la clase)
        self.__titular = titular
        self.__saldo = saldo_inicial

    # Método público para mostrar información de la cuenta
    def mostrar_informacion(self):
        print(f"Titular: {self.__titular} - Saldo actual: ${self.__saldo}")

    # Método público para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"✅ Depósito de ${cantidad} realizado correctamente.")
        else:
            print("⚠️ La cantidad a depositar debe ser positiva.")

    # Método público para retirar dinero
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"💸 Retiro de ${cantidad} realizado correctamente.")
        else:
            print("❌ Fondos insuficientes o cantidad inválida.")

# ------------------------------------------------------------------------------
# Uso de la clase (programa principal)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Creamos un objeto de tipo CuentaBancaria
    cuenta = CuentaBancaria("Mercy Nogales", 500)

    # Mostramos la información inicial
    cuenta.mostrar_informacion()

    # Realizamos algunas operaciones
    cuenta.depositar(200)
    cuenta.retirar(100)
    cuenta.retirar(700)  # Esto mostrará un mensaje de error

    # Mostramos la información final
    cuenta.mostrar_informacion()

    print("\n✅ Ejemplo de encapsulación ejecutado correctamente.")
