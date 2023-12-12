#include <stdio.h>
#include <string.h>

void main() {
    char baris1[50],baris2[50];

    scanf(" %[^\n]", &baris1);

    scanf(" %[^\n]", &baris2);

    printf("\n");

    size_t SIZE_baris1 = strlen(baris1);
    size_t SIZE_baris2 = strlen(baris2);

    if(SIZE_baris1 == SIZE_baris2) {

        size_t i = 0;
        size_t j = 0;

        int JUMLAH_ASTERISK = 0;
        int JUMLAH_HASH = 0;

        while(i < SIZE_baris1 && j < SIZE_baris2) {

            if(baris1[i] == ' ' && baris2[j] == ' '){
                i++;
                j++;
                continue;
            }
            if(baris1[i] == baris2[j]) {
                printf("*");
                JUMLAH_ASTERISK++;
            }
            else {
                printf("#");
                JUMLAH_HASH++;
            }
            i++;
            j++;
        }

        printf("\n* = %d\n", JUMLAH_ASTERISK);
        printf("# = %d\n", JUMLAH_HASH);

        if (JUMLAH_ASTERISK >= JUMLAH_HASH) {
            printf("Pesan Asli");
        }
        else {
            printf("Pesan Palsu");
        }

    }

    else {
        printf("Panjang kalimat berbeda, pesan palsu");
    } 
}
