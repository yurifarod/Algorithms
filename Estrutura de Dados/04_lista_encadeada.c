#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
	c.dado é o dado de uma struct
	p->dado é o dado de um ponteiro de struct

	Proxima aual entramos com as REMOÇÕES!
	Para este exercicio vamos desenvolver um sistema com um Menu com as opções
	s -> sair
	i -> inserir novo aluno
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

void insere(char nome[100], char curso[100], int matricula, Aluno **cabeca){
	if(*cabeca == NULL){
		*cabeca = (Aluno *) malloc(sizeof(Aluno));
  		strcpy((*cabeca)->nome, nome);
  		strcpy((*cabeca)->curso, curso);
  		(*cabeca)->matricula = matricula;
        (*cabeca)->prox = NULL;
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
  	printf("%d Aluno teve sua insercao concluida!\n", matricula);
}

void imprime(Aluno **cabeca){
	printf("========= RELATORIO DE ALUNOS =========\n");
	Aluno *p = (*cabeca);
	while(p != NULL){
		printf("%d\n", p->matricula);
		printf("%s\n", p->nome);
		printf("%s\n", p->curso);
		printf("====================\n");
		p = p->prox;
	}
}

int main() { 
	
	Aluno *cabeca = NULL;

	insere("Joao dos Santos", "Analise e Desenvolvimento de Sistemas", 2023001, &cabeca);
	insere("Jose dos Almeida", "Analise e Desenvolvimento de Sistemas", 2023002, &cabeca);
	insere("Maria dos Santos", "Analise e Desenvolvimento de Sistemas", 2023003, &cabeca);
	insere("Sonia de Jesus", "Analise e Desenvolvimento de Sistemas", 2023004, &cabeca);

	imprime(&cabeca);
	
	return 0;
}
