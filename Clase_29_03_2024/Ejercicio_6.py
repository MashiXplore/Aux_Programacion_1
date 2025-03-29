# 6. Realice la función, para calcular el valor de aproximado de π (Serie de Nilakantha), según la serie:
def intriducir():
    n = int(input("Introducir n: "))
    return n

def genera_serie(n):
    contador_1 = 0
    contador_2 = 2
    resultado = 3
    for i in range(n):
        if contador_1 % 2 == 0:
            contador_2 = multiplica_3(contador_2)
            resultado = resultado + (4/contador_2)
        else:
            contador_2 = multiplica_3(contador_2)
            resultado = resultado - (4/contador_2)
        contador_1 += 1
        return resultado
        
def multiplica_3(contador_2):
    a = 1
    for i in range(3):
        a = a * contador_2
        contador_2 += 1
    return a

def main():
    n = intriducir()
    print(f"El resultado es: {genera_serie(n)}")

main()