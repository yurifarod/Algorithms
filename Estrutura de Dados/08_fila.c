#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
	Exercicio! Transformar este codigo em um que possua uma fila preferencial!
	E chamado um cliente da preferencial a cada cliente da lista normal
	Um novo campo idade deverá ser incluido e os clientes sao inseridos na preferencial
	se tiverem mais de 60 anos!
*/

typedef struct tipo_cliente {
	int senha;
	char nome[100];
	int nrconta;
	struct tipo_cliente *anterior;
} Cliente;

void iniciar(Cliente **inicio, Cliente **fim){
	*inicio = NULL;
	*fim = NULL;
}

void insere(int senha, char nome[100], int nrconta, Cliente **inicio, Cliente **fim){
	if(*fim == NULL){
		*inicio = (Cliente *) malloc(sizeof(Cliente));
		(*inicio)->anterior = NULL;


		*fim = (Cliente *) malloc(sizeof(Cliente));
		(*fim)->anterior = NULL;

		Cliente *novo;
		novo = (Cliente *) malloc(sizeof(Cliente));
	  	strcpy(novo->nome, nome);
	  	novo->nrconta = nrconta;
	  	novo->senha = senha;
	  	novo->anterior = NULL;
	  	(*inicio)->anterior = novo;
	  	(*fim)->anterior = novo;
	}
	else{
		Cliente *novo;
		novo = (Cliente *) malloc(sizeof(Cliente));
	  	strcpy(novo->nome, nome);
	  	novo->nrconta = nrconta;
	  	novo->senha = senha;
	  	novo->anterior = NULL;
	  	(*fim)->anterior->anterior = novo;
	  	(*fim)->anterior = (*fim)->anterior->anterior;
  	}
  	printf("%s - Cliente alocado no final da fila!\n", nome);
}

void imprime(Cliente **inicio){
	printf("\n\n========= FILA =========\n");
	Cliente *p = (*inicio);
	p = p->anterior;
	while(p != NULL){
		printf("Senha: %d, Nome: %s\n",p->senha, p->nome);
		p = p->anterior;
	}
	printf("========= FILA =========\n");	
}

int remover_elemento(Cliente **inicio){

	Cliente *delete = (*inicio)->anterior;

	char nome_del[100];
	strcpy(nome_del, delete->nome);
	int senha_del = delete->senha;

	(*inicio)->anterior = delete->anterior;

	printf("%s\n", delete->nome);
	free(delete);
	delete = NULL;

	printf("Cliente chamado: %s, senha: %d\n", nome_del, senha_del);

	return 1;
}



int main() { 
	
	Cliente *inicio;
	Cliente *fim;

	iniciar(&inicio, &fim);

	int senha = 0;

	insere(1, "Joao dos Santos", 2023001, &inicio, &fim);
	insere(2, "Jose dos Almeida", 2023002, &inicio, &fim);
	insere(3, "Maria dos Santos", 2023003, &inicio, &fim);
	remover_elemento(&inicio);
	insere(4, "Sonia de Jesus", 2023004, &inicio, &fim);
	remover_elemento(&inicio);
	insere(5, "Armando Saraiva", 2023005, &inicio, &fim);
	imprime(&inicio);

	return 0;
}