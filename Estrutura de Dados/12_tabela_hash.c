#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
	c.dado é o dado de uma struct
	p->dado é o dado de um ponteiro de struct
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
void iniciar_lista(Aluno **lista, int size){
	for(int i = 0; i < size; i++){
		iniciar(&lista[i]);
	}
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

void imprime_lista(Aluno **lista, int size){
	printf("\n\n========= RELATORIO DE ALUNOS =========\n");
	for(int i = 0; i < size; i++){
		if(lista[i] != NULL){
			imprime(&lista[i]);			
		}
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

int funcao_dispersao(int matricula, int size){
	return matricula % size;
}

int main() { 
	
	int size = 10;
	Aluno *lista[size];

	iniciar_lista(lista, size);

	insere("Antonia dos Santos", "Analise e Desenvolvimento de Sistemas", 2023000, &lista[funcao_dispersao(2023000, size)]);
	insere("Joao dos Santos", "Analise e Desenvolvimento de Sistemas", 2023001, &lista[funcao_dispersao(2023001, size)]);
	insere("Jose dos Almeida", "Analise e Desenvolvimento de Sistemas", 2023002, &lista[funcao_dispersao(2023002, size)]);
	insere("Maria dos Santos", "Analise e Desenvolvimento de Sistemas", 2023003, &lista[funcao_dispersao(2023003, size)]);
	insere("Sonia de Jesus", "Analise e Desenvolvimento de Sistemas", 2023004, &lista[funcao_dispersao(2023004, size)]);
	insere("Armando Saraiva", "Analise e Desenvolvimento de Sistemas", 2023005, &lista[funcao_dispersao(2023005, size)]);
	insere("Thiago Andre", "Analise e Desenvolvimento de Sistemas", 2023011, &lista[funcao_dispersao(2023011, size)]);
	insere("Silvio Santos", "Analise e Desenvolvimento de Sistemas", 2023014, &lista[funcao_dispersao(2023014, size)]);
	insere("Eustaquio Andrade", "Analise e Desenvolvimento de Sistemas", 2023006, &lista[funcao_dispersao(2023006, size)]);

	imprime_lista(lista, size);

	buscar(2023004, &lista[funcao_dispersao(2023004, size)]);

	remover_elemento(2023004, &lista[funcao_dispersao(2023004, size)]);

	imprime_lista(lista, size);

	return 0;
}