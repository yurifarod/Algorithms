#include<stdio.h>
#include<stdlib.h>

void quicksort(int *vetor, int inicio, int final)
{
	int i, j, pivo, aux;
	i = inicio;
	j = final-1;
	pivo = vetor[(inicio + final) / 2];
	while(i <= j)
	{
		while(vetor[i] < pivo && i < final)
		{
			i++;
		}
		while(vetor[j] > pivo && j > inicio)
		{
			j--;
		}
		if(i <= j)
		{
			aux = vetor[i];
			vetor[i] = vetor[j];
			vetor[j] = aux;
			i++;
			j--;
		}
	}
	if(j > inicio){
		quicksort(vetor, inicio, j+1);
	}
	if(i < final){
		quicksort(vetor, i, final);
	}
}

int main()
{
	int tam = 10;

	int vetor[10] = {5, 8, 1, 2, 7, 3, 6, 9, 4, 10};

	quicksort(vetor, 0, tam);

	for(int i = 0; i < tam; i++){
        printf("%d ",vetor[i]);
    }

	return 0;
}