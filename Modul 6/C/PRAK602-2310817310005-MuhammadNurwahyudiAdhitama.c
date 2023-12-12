#include <stdio.h>

void main() {
    int TOTAL;

    scanf("%d", &TOTAL);
    
    int arr[TOTAL];

    for(int i = 0 ; i < TOTAL ; i++) {
        scanf("%d", &arr[i]);
    }
    
    for(int i = 0 ; i < TOTAL ; i++) {
        arr[i] = arr[i] * (1 + i);
        printf("%d ", arr[i]);
    }
}