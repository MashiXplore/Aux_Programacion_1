# 3. Realiza una función para calcular el área y otra función para calcular el perímetro de un triángulo equilátero: 

def intruducir_datos():
    base = int(input("Ingrese la Base: "))
    altura = int(input("Ingrese el altura: "))
    return base,altura

def calcular_area(base,altura):
    area = (base * altura) / 2
    print(f"El area es: {area}")
    
def calcular_perimetro(lado):
    perimetro = lado + lado + lado
    print(f"El Perimetro es: {perimetro}")
    
def main():
    base , altura = intruducir_datos()
    calcular_area(base,altura)
    calcular_perimetro(base)
    
main()