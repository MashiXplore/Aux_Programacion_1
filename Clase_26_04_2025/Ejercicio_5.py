# a) Implementa Bubble Sort.
def bubble_sort(vector, reverse=False):
    n = len(vector)
    for i in range(n):
        for j in range(0, n-i-1):
            if (vector[j] > vector[j+1]) != reverse:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector

def ordenar_mitad_bubble(vector_original):
    mitad = len(vector_original) // 2
    izquierda = bubble_sort(vector_original[:mitad], reverse=False)
    derecha = bubble_sort(vector_original[mitad:], reverse=True)
    return izquierda + derecha

print("Bubble sort")
vector = [5, 2, 8, 1, 9, 7, 4, 6]
print("Vector DEsordenado: ",vector)
print("Vector ordenado Bubble Sort: ",ordenar_mitad_bubble(vector))

# b) Implementa Selection Sort.
def selection_sort(vector, reverse=False):
    n = len(vector)
    for i in range(n):
        idx = i
        for j in range(i+1, n):
            if (vector[j] < vector[idx]) != reverse:
                idx = j
        vector[i], vector[idx] = vector[idx], vector[i]
    return vector

def ordenar_mitad_selection(vector_original):
    mitad = len(vector_original) // 2
    izquierda = selection_sort(vector_original[:mitad], reverse=False)
    derecha = selection_sort(vector_original[mitad:], reverse=True)
    return izquierda + derecha

print("Select Sort")
vector = [5, 2, 8, 1, 9, 7, 4, 6]
print("Vector DEsordenado: ",vector)
print("Vector ordenado Select Sort: ",ordenar_mitad_selection(vector))


# c) Implementa Insert Sort.
def insertion_sort(vector, reverse=False):
    for i in range(1, len(vector)):
        key = vector[i]
        j = i-1
        while j >=0 and (vector[j] > key) != reverse:
            vector[j+1] = vector[j]
            j -= 1
        vector[j+1] = key
    return vector

def ordenar_mitad_insertion(vector_original):
    mitad = len(vector_original) // 2
    izquierda = insertion_sort(vector_original[:mitad], reverse=False)
    derecha = insertion_sort(vector_original[mitad:], reverse=True)
    return izquierda + derecha

print("Insert Sort")
vector = [5, 2, 8, 1, 9, 7, 4, 6]
print("Vector DEsordenado: ",vector)
print("Vector ordenado Insert Sort: ",ordenar_mitad_insertion(vector))
