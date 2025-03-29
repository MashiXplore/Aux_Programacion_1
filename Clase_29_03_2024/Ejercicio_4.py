#Realiza una función para calcular el área y otra función para calcular el perímetro de un círculo (use pi=3.1416):
def intruducir_datos():
    radio = int(input("Ingrese El Radio del ciculo: "))
    return radio

def calcular_area(radio):
    pi = 3.1416
    area = pi * (radio*radio)
    print(f"El area es: {area}")
    
def calcular_perimetro(radio):
    pi = 3.1416
    perimetro = 2 * pi * radio
    print(f"El Perimetro es: {perimetro}")
    
def main():
    radio = intruducir_datos()
    calcular_area(radio)
    calcular_perimetro(radio)
    
main()