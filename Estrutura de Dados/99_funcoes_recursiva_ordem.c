#include <stdio.h>

int dec1(int n, int c){
	if(n < 1){
		return 1;
	}
	printf("Executado %d na instancia %d\n", n, c);
	dec1(n-1, c);
}
int dec2(int n, int c){
	if(n < 1){
		return 1;
	}
	printf("Executado %d na instancia %d\n", n, c);
	dec2(n-1, c);
}
int funcao(int n, int c){
	printf("Iniciando funcao conjunta\n");
	dec1(n-1, 1);
	dec2(n-1, 2);
}
int main(){
	int resultado, entrada;

	scanf("%d", &entrada);

	funcao(entrada, 0);

	return 0;
}
