import numpy as np

baris1, baris2 = map(int, input("").split())

if (baris1 == baris2) :

    E_ARRAY1 = list(map(int,input("").split()))
    E_ARRAY2 = list(map(int,input("").split()))

    arr1 = np.array(E_ARRAY1).reshape(1,baris1)
    arr2 = np.array(E_ARRAY2).reshape(1,baris2)

    i = 0
    
    while i < baris1 and i < baris2 :
        HASIL = E_ARRAY1[i] * E_ARRAY2[i]
        print(HASIL, end = " ")
        i += 1

else :
    print("Jumlah tidak sama")