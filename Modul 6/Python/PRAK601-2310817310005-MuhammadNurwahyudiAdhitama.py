import numpy as np

V, H = map(int, input().split())

E_ARRAY = list(map(int,input().split(" ")))

arr = np.array(E_ARRAY).reshape((V, H))

for HASIL in arr :
    print(*HASIL)   
