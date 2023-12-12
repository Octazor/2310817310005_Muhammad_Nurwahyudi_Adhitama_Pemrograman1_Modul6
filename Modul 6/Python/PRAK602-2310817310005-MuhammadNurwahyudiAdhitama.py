import numpy as np

TOTAL = int(input(""))

E_ARRAY = list(map(int,input("").split()))

arr = np.array(E_ARRAY).reshape((1,TOTAL))

i = 0

while i < TOTAL :
    HASIL = E_ARRAY[i] * (i + 1)
    print(f"{HASIL}", end = " ")
    i += 1