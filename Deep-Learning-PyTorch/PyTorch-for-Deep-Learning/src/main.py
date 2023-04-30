# import torch
# import subprocess

# Definición de una clase
class Animal:
    # Método de inicialización
    def __init__(self, nombre):
        self.nombre = nombre

    # Método para imprimir el nombre del animal
    def imprimir_nombre(self):
        print("El nombre del animal es", self.nombre)

# Crear una instancia de la clase Animal
mi_animal = Animal("Gato")
# Llamar al método imprimir_nombre de la instancia
mi_animal.imprimir_nombre()
# Definir una función que reciba dos argumentos y devuelva su suma
def suma(a, b):
    return a + b

# Llamar a la función suma y almacenar el resultado en una variable
resultado = suma(3, 5)

# Imprimir el resultado
print("La suma de 3 y 5 es:", resultado)
