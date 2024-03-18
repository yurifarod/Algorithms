#include <stdio.h>
#include <stdlib.h> //necessário para usar as funções malloc() e free()
#include <conio.h>
int main(void)
{
  float *v; //definindo o ponteiro v
  int i, num_componentes;
  
  printf("Informe o numero de componentes do vetor\n");
  scanf("%d", &num_componentes);
  
  /* ------------- Alocando dinamicamente o espaço necessário -------------
  
  1 - Calcular o número de bytes necessários
  primeiramente multiplicamos o número de componentes do vetor pela
  quantidade de bytes que é dada pelo comando sizeof,
  portanto temos:
  num_componentes * sizeof(float)
  
  2 - Reservar a quantidade de memória
  usamos malloc para reservar essa quantidade de memória,
  então temos:
  malloc(num_componentes * sizeof(float))
  
  3 - Converter o ponteiro para o tipo de dados desejado
  como a função malloc retorna um ponteiro do tipo void,
  precisamos converter esse ponteiro para o tipo da nossa variável, no caso float,
  por isso usamos o comando de conversão explicita:
  (float *)
  
  4 - juntando tudo e atribuindo em v temos o comando abaixo: */
  
  v = (float *) malloc(num_componentes * sizeof(float));
  
  //Armazenando os dados em um vetor
  for (i = 0; i < num_componentes; i++)
  {
    printf("\nDigite o valor para a posicao %d do vetor: ", i+1);
    scanf("%f",&v[i]);
  }
  
  // ------ Percorrendo o vetor e imprimindo os valores ----------
  printf("\n*********** Valores do vetor dinamico ************\n\n");
  
  for (i = 0;i < num_componentes; i++)
  {
    printf("%.2f\n",v[i]);
  }
  
  //liberando o espaço de memória alocado
  free(v);
  
  //Funcao muito utilizada para pausar o terminal e aguardar uma entrada
  getch();
  return 0;
}