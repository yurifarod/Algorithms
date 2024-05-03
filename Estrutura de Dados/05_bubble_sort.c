#include<stdio.h>
#include<stdlib.h>
void trocar(int *a, int *b){ 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 
void bubbleSort(int *vetor, int n){ 
    if (n < 1)return; 
 
    for (int i=0; i<n; i++){
        if (vetor[i] > vetor[i+1]) {
            trocar(&vetor[i], &vetor[i+1]);  
        }
    }
    bubbleSort(vetor, n-1); 
} 

int main(){
    int tam = 10;

    int vetor[10] = {5,8,1,6,9,0,3,2,7,4};

    bubbleSort(vetor,tam-1);
    
    for(int i = 0; i < tam; i++){
    	printf("%d ",vetor[i]);
    }
    
    return 0;
}