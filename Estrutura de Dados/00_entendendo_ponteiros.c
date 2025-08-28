#include <stdio.h>
int main(){

	//Variavel "a" do tipo inteiro
	int a = 5;

	//variavel "b" que armazena um endereço de memória de inteiro
	int *b = &a;

	printf("Valor armazenado na variavel a: %d\n", a);
	printf("Valor armazenado na variavel a: %d\n", *b);

	printf("Endereco de memoria da variavel a: %d\n", b);
	printf("Endereco de memoria da variavel a: %d\n", &a);
	
	return 0;
}
