# PROGRAMACION MODULAR
# 1. Realiza una función para calcular el área y otra función para calcular el perímetro de un cuadrado:

def introducir():
    lado = int(input("Ingrese el Lado: "))
    return lado

def calcula_area(lado):
    area = lado * lado
    return area

def calcula_perimetro(lado):
    perimetro = lado + lado + lado + lado
    return perimetro



lado = introducir()
print(f"El area es: {calcula_area(lado)}")
print(f"El perimetro es: {calcula_perimetro(lado)}")
    

    

