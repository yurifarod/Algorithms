#include <stdio.h>

int fatorial(int n){
	if(n == 1){
		return 1;
	}
	return n*fatorial(n-1);
}
int main(){
	int resultado, entrada;

	scanf("%d", &entrada);

	resultado = fatorial(entrada);

	printf("%d\n", resultado);

	return 0;
}
