def bubble_sort(vector):
    n = len(vector)
    intercambios = 0
    for i in range(n):
        for j in range(0,n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j],vector[j+1] = vector[j+1],vector[j]
                intercambios+=1
    return vector,intercambios

vector = [10,2,63,2,4,95,32,11]
print("Vector Desordenado: ",vector)
nuevo_vector,intercambio = bubble_sort(vector)
print("Vector Ordenado: ",nuevo_vector)
print("Numero de intercambios realizados: ",intercambio)

