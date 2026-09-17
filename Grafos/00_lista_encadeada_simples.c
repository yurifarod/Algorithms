#include <stdio.h>
#include <stdlib.h>

struct No {
    int dado;
    struct No *proximo;
};

int main() {

    struct No *inicio = NULL;

    struct No *n1 = malloc(sizeof(struct No));
    struct No *n2 = malloc(sizeof(struct No));
    struct No *n3 = malloc(sizeof(struct No));

    n1->dado = 10;
    n2->dado = 20;
    n3->dado = 30;

    n1->proximo = n2;
    n2->proximo = n3;
    n3->proximo = NULL;

    inicio = n1;

    struct No *atual = inicio;

    while (atual != NULL) {
    	printf("%d\n", atual->dado);
    	atual = atual->proximo;
	}

    return 0;
}