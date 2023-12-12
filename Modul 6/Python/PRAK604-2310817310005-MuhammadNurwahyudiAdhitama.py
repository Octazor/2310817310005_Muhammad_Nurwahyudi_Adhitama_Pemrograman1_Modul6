import numpy as np

baris1 = input("")
baris2 = input("")

print()

arr1 = np.array(baris1).reshape(1,1)
arr2 = np.array(baris2).reshape(1,1)

SIZE_baris1 = len(baris1)
SIZE_baris2 = len(baris2)

if (SIZE_baris1 == SIZE_baris2) :

    i = 0
    j = 0
    JUMLAH_ASTERISK = 0
    JUMLAH_HASH = 0

    while (i < SIZE_baris1 and j < SIZE_baris2) :
        
        if (baris1[i] == ' ' and baris2[j] == ' ') :
            i += 1
            j += 1
            continue

        if (baris1[i] == baris2[j]) :
            print("*", end = "")
            JUMLAH_ASTERISK += 1

        else :
            print("#", end = "")
            JUMLAH_HASH += 1

        i += 1
        j += 1

    print(f"\n* = {JUMLAH_ASTERISK}")
    print(f"# = {JUMLAH_HASH}")

    if (JUMLAH_ASTERISK >= JUMLAH_HASH) :
        print("Pesan Asli")
    
    else :
        print("Pesan Palsu")
        
else :
    print("Panjang kalimat berbeda, pesan palsu")