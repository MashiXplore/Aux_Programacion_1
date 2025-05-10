import random
import time

n = 20000
vector = [random.randint(0,20000) for _ in range(n)]

def selection_sort(vector):
  for i in range(len(vector)):
    min_idx = i
    for j in range(i+1, len(vector)):
      if vector[j] < vector[min_idx]:
        min_idx = j
      vector[i],vector[min_idx] = vector[min_idx],vector[i]

inicio = time.time()
selection_sort(vector.copy())
fin = time.time()

print(f"Tiempo de ordenamiento con seleciotion_sort: {fin - inicio:.2f} segundos")
        