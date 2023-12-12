#include <stdio.h>

int main() {
    int baris1, baris2;

    scanf("%d %d", &baris1, &baris2);

    
    if (baris1 == baris2) {
        int arr1[baris1];
        int arr2[baris2];

        for (int i = 0; i < baris1; i++) {
            scanf("%d", &arr1[i]);
        }

        for (int i = 0; i < baris2; i++) {
            scanf("%d", &arr2[i]);
        }

        for (int i = 0; i < baris1 && i < baris2; i++) {
            int hasil = arr1[i] * arr2[i];
            printf("%d ", hasil);
        }
        printf("\n");
    } else {
        printf("Jumlah elemen tidak sama.\n");
    }

    return 0;
}
