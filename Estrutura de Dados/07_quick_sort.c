#include<stdio.h>
#include<stdlib.h>

void quicksort(int values[], int began, int end)
{
	int i, j, pivo, aux;
	i = began;
	j = end-1;
	pivo = values[(began + end) / 2];
	while(i <= j)
	{
		while(values[i] < pivo && i < end)
		{
			i++;
		}
		while(values[j] > pivo && j > began)
		{
			j--;
		}
		if(i <= j)
		{
			aux = values[i];
			values[i] = values[j];
			values[j] = aux;
			i++;
			j--;
		}
	}
	if(j > began)
		quicksort(values, began, j+1);
	if(i < end)
		quicksort(values, i, end);
}

int main(int argc, char *argv[])
{
	int tam = 10;

	int v[10] = {5, 8, 1, 2, 7, 3, 6, 9, 4, 10};

	quicksort(v, 0, tam);

	for(int i = 0; i < tam; i++){
        printf("%d ",v[i]);
    }

	return 0;
}