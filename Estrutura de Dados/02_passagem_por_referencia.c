#include <stdio.h>
void troca(int *x, int *y) { 
	int aux;
	if(x != NULL && y != NULL){ //se endereços forem válidos 
	aux = *x; //faz a troca
	*x = *y;
	*y = aux;
}
}
int main(){
	int v1=5, v2=10;
	printf("Antes, v1 = %d e v2 = %d\n", v1, v2);
	troca(&v1, &v2);
	printf("Depois, v1 = %d e v2 = %d\n", v1, v2);
	return 0;
}
