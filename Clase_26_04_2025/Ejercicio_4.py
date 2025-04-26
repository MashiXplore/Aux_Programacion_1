def bubble_sort_pares(v):
    indices = [i for i in range(len(v)) if i%2==0]
    
    for i in range(len(indices)):
        for j in range(0,len(indices)-i -1):
            if v[indices[j]] > v[indices[j+1]]:
                v[indices[j]],v[indices[j+1]] = v[indices[j+1]],v[indices[j]]
    return v

vector = [8,3,7,2,5,4,6]
print("Vector Desordenado: ",vector)
print("Vector ordeando solo posiciones pares: ",bubble_sort_pares(vector))