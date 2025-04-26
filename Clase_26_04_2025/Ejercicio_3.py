def bubble_sort_multiplos(v):
    indices = [i for i in range(len(v)) if v[i]%5==0]
    
    for i in range(len(indices)):
        for j in range(0,len(indices)-i -1):
            if v[indices[j]] > v[indices[j+1]]:
                v[indices[j]],v[indices[j+1]] = v[indices[j+1]],v[indices[j]]
    return v

vector = [10,3,5,7,15,2,25]
print("Vector Desordenado: ",vector)
print("Vector Ordenado solo multiplos de 5: ",bubble_sort_multiplos(vector))