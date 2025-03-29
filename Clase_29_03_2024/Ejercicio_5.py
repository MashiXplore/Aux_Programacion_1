# 5. Realice la función, para calcular el valor de aproximado de π (Serie de Leibniz), según la serie:

def intriducir():
    n = int(input("Introducir n: "))
    return n

def genera_serie(n):
    contado_1 = 0
    contado_2 = 1
    resultado = 0
    for i in range(n):
        if contado_1 % 2 == 0:
            resultado = resultado + (4/contado_2)
        else:
            resultado = resultado - (4/contado_2)
        contado_1 += 1
        contado_2 += 2
    return resultado

def main():
    n = intriducir()
    print(f"El resultado es: {genera_serie(n)}")
    
main()