import time
import random

x = int(input("Ingresa el numero a buscar: "))
n = 10000
vector = [random.randint(0,1000) for _ in range(n)]

inicio = time.time()
encontrado = False
for num in vector:
  if num == x: 
    encontrado = True
    break

fin = time.time()

print(f"Elemento Encontrado")
print(f"Tiempo de busqueda lineal: {fin - inicio:.6f} milisegundos")