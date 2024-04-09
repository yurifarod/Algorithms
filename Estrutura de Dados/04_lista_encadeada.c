#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
	c.dado é o dado de uma struct
	p->dado é o dado de um ponteiro de struct

	Para este exercicio vamos desenvolver um sistema com um Menu com as opções
	s -> sair
	i -> inserir novo aluno
 	d -> deletar aluno
	r -> relatorio de alunos
	Qualquer outro caractere deverá reiniciar o menu
	Ao final do uso o arquivo deverá ser reescrito com todos os registros

*/

typedef struct tipo_aluno {
	int matricula;
	char nome[100];
	char curso[100];
	struct tipo_aluno *prox;
} Aluno;

void iniciar(Aluno **cabeca){
	*cabeca = NULL;
}

void insere(char nome[100], char curso[100], int matricula, Aluno **cabeca){
	if(*cabeca == NULL){
		*cabeca = (Aluno *) malloc(sizeof(Aluno));
        (*cabeca)->prox = NULL;

		Aluno *novo;
		novo = (Aluno *) malloc(sizeof(Aluno));
	  	strcpy(novo->nome, nome);
	  	strcpy(novo->curso, curso);
	  	novo->matricula = matricula;
	  	novo->prox = (*cabeca)->prox;
	  	(*cabeca)->prox = novo;
	}
	else{
		Aluno *novo;
		novo = (Aluno *) malloc(sizeof(Aluno));
	  	strcpy(novo->nome, nome);
	  	strcpy(novo->curso, curso);
	  	novo->matricula = matricula;
	  	novo->prox = (*cabeca)->prox;
	  	(*cabeca)->prox = novo;
  	}
  	printf("%d - Aluno teve sua insercao concluida!\n", matricula);
}

void imprime(Aluno **cabeca){
	printf("\n\n========= RELATORIO DE ALUNOS =========\n");
	Aluno *p = (*cabeca);
	p = p->prox;
	while(p != NULL){
		printf("%d\n", p->matricula);
		printf("%s\n", p->nome);
		printf("%s\n", p->curso);
		printf("====================\n");
		p = p->prox;
	}
}

Aluno* buscar(int matricula, Aluno **cabeca){
	Aluno *p = (*cabeca);
	
	if(p == NULL){
		return NULL;
	}

	while(p != NULL){
		if(p->matricula == matricula){
			printf("### Aluno encontrado ###\n");
			printf("%d\n", p->matricula);
			printf("%s\n", p->nome);
			printf("%s\n", p->curso);
			return p;
			break;
		}
		p = p->prox;
	}

	return NULL;
}

/*Esse metodo foi desenvolvido para dar clareza a busca e ao entendimento do codigo*/
Aluno* buscar_anterior(int matricula, Aluno **cabeca){
	Aluno *p = (*cabeca);
	Aluno *ant = NULL;

	if(p == NULL){
		return NULL;
	}

	while(p != NULL){
		if(p->matricula == matricula){
			printf("### Aluno encontrado ###\n");
			printf("%d\n", ant->matricula);
			printf("%s\n", ant->nome);
			printf("%s\n", ant->curso);
			return ant;
			break;
		}
		ant = p;
		p = p->prox;
	}

	return NULL;
}

int remover_elemento(int matricula, Aluno **cabeca){

	Aluno *anterior = buscar_anterior(matricula, cabeca);
	Aluno *delete = buscar(matricula, cabeca);

	// se for NULL, é porque não existe, então retorna 0
	if(delete == NULL){
		printf("Aluno nao cadastrado na base!\n");
		return 0;
	}
	if(anterior != NULL){
		anterior->prox = delete->prox;
	}
	if(delete == (*cabeca) ){
		(*cabeca) = delete->prox;
	}

	free(delete);
	delete = NULL;

	printf("Matricula - %d, removida com sucesso\n", matricula);

	return 1;
}



int main() { 
	
	Aluno *cabeca;

	iniciar(&cabeca);

	insere("Joao dos Santos", "Analise e Desenvolvimento de Sistemas", 2023001, &cabeca);
	insere("Jose dos Almeida", "Analise e Desenvolvimento de Sistemas", 2023002, &cabeca);
	insere("Maria dos Santos", "Analise e Desenvolvimento de Sistemas", 2023003, &cabeca);
	insere("Sonia de Jesus", "Analise e Desenvolvimento de Sistemas", 2023004, &cabeca);
	insere("Armando Saraiva", "Analise e Desenvolvimento de Sistemas", 2023005, &cabeca);

	imprime(&cabeca);

	buscar(2023004, &cabeca);
	buscar_anterior(2023004, &cabeca);

	remover_elemento(2023004, &cabeca);

	imprime(&cabeca);

	return 0;
}