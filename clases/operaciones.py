import math

class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1:"))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2:"))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def sumar(self):
        self.resultado = "La suma de " + str(self.num1) + " + " + str(self.num2) + " es igula a " + str(self.num1 + self.num2)

    #operación de restar
    def resta(self):
        self.resultado = "La resta de " + str(self.num1) + " - " + str(self.num2) + " es igula a " + str(self.num1 - self.num2)

    #operación de multiplicación
    def multiplicacion(self):
        self.resultado = "La multiplicación de " + str(self.num1) + " x " + str(self.num2) + " es igula a " + str(self.num1 * self.num2)

    #operación de división
    def division(self):
        self.resultado = "La división de " + str(self.num1) + " / " + str(self.num2) + " es igula a " + str(self.num1 / self.num2)
    
    def mostrarResultado(self):
        print(self.resultado)
        
        
