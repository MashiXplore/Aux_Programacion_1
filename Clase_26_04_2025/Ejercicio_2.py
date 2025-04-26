def bubble_sort_cadenas(vector):
    n = len(vector)
    for i in range(n):
        for j in range(0,n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j],vector[j+1] = vector[j+1],vector[j]
    return vector

vector = ["manzana","Limas","Pera","Tomate","zapallo","Palta"]
print("Vector Desordenado: ",vector)
print("Vector Ordenado: ",bubble_sort_cadenas(vector))

