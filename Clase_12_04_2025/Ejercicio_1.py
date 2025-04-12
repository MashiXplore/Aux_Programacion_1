matrices = [
    [1,2,3,1,3,44556,345,2,1,3],
    [4,5,6],
    [7,8,9,10,50]]

for i in range(len(matrices)):
    for j in range(len(matrices[i])):
        print(f"{matrices[i][j]}",end=" ")
    print()

#Ejercico realizar que muestre en pisicones pares el numero 0
for i in range(len(matrices)):
    for j in range(len(matrices[i])):
        if not j % 2 == 0:
            matrices[i][j] = 0

print("Matris modificada con pares a 0")
for i in range(len(matrices)):
    for j in range(len(matrices[i])):
        print(f"{matrices[i][j]}",end=" ")
    print()