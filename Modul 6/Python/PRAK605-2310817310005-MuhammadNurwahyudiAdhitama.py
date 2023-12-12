import numpy as np

ordo = int(input("Masukkan jumlah ordo matriks : "))

print("Matriks A:")
E_ARRAY1 = []
for i in range(ordo):
    BARIS = list(map(int, input("").split()))
    E_ARRAY1.append(BARIS)

print("Matriks B:")
E_ARRAY2 = []
for i in range(ordo):
    BARIS = list(map(int, input("").split()))
    E_ARRAY2.append(BARIS)

arr1 = np.array(E_ARRAY1).reshape(ordo,ordo)
arr2 = np.array(E_ARRAY2).reshape(ordo,ordo)

print("Matriks AXB : ")

PERKALIAN = np.dot(arr1, arr2)

for HASIL in PERKALIAN :
    print(*HASIL) 
