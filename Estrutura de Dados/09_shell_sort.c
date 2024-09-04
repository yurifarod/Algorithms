#include <stdio.h>

void shellSort(int *vet, int size) {
    int i, j, value;
 
    int h = 1;
    while(h < size) {
        h = 3*h+1;
    }
    while (h > 0) {
        for(i = h; i < size; i++) {
            value = vet[i];
            j = i;
            while (j > h-1 && value <= vet[j - h]) {
                vet[j] = vet[j - h];
                j = j - h;
            }
            vet[j] = value;
        }
        h = h/3;
    }
}

int main(){
    int tam = 10;

    int vetor[10] = {5,8,1,6,9,0,3,2,7,4};

    shellSort(vetor,tam);
    
    for(int i = 0; i < tam; i++){
        printf("%d ",vetor[i]);
    }
    
    return 0;
}