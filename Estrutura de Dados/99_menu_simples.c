#include <stdio.h>

int main(){
	char menu = 'X';

	printf("Digite a opcao desejada\n");
	printf("A - Opcao A\n");
	printf("B - Opcao B\n");
	printf("C - Opcao C\n");
	printf("S - Sair\n");

	while(menu != 'S'){
		scanf(" %c", &menu);

		if(menu == 'A'){
			printf("Opcao A escolhida!\n");
		}
		if(menu == 'B'){
			printf("Opcao B escolhida!\n");
		}
		if(menu == 'C'){
			printf("Opcao C escolhida!\n");
		}
		if(menu == 'S'){
			printf("Obrigado por usar o programa...!");
		}
		if(menu != 'A' && menu != 'B' && menu != 'C' && menu != 'S' ){
			printf("Opcao invalida, tente novamente!\n");
		}
	}

	return 0;
}