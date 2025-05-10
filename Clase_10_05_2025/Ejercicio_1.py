import random
import time

n = 100000
vector = [random.randint(0,20000) for _ in range(n)]

def bubble_sort(vector):
    for i in range(len(vector)):
      for j in range(0,len(vector) - i - 1):
        if vector[j] > vector[j+1]:
          vector[j], vector[j+1] = vector[j+1], vector[j]

inicio = time.time()
bubble_sort(vector.copy())
fin = time.time()

print(f"Tiempo de ordenamiento con Bubble_sort: {fin - inicio:.2f} segundos")
        