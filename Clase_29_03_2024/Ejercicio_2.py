# PROGRAMACION MODULAR
# 2. Realiza una función para calcular el área y otra función para calcular el perímetro de un paralelepípedo:
# area = b * a
# perimetro  = 2(a+b)
def intruducir_datos():
    base = int(input("Ingrese la Base: "))
    altura = int(input("Ingrese el altura: "))
    return base,altura

def calcular_area(base,altura):
    area = base * altura
    print(f"El area es: {area}")
    
def calcular_perimetro(base,altura):
    perimetro = 2 * (base + altura)
    print(f"El Perimetro es: {perimetro}")
    
def main():
    base , altura = intruducir_datos()
    calcular_area(base,altura)
    calcular_perimetro(base,altura)
    
main()