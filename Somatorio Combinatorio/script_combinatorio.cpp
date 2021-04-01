#include <stdio.h>
#include <stdlib.h>

using namespace std;
int main(){

  int size = 0;
  float total = 0;
  float total_it = 0;
  FILE *arq;

  arq = fopen("entradas.input", "r");
  fscanf(arq, "%d", &size);
  fscanf(arq, "%f", &total);

  float valor[200];

  for(int i = 0; i < size; i++){
    fscanf(arq,"%f", &valor[i]);
  }
  fclose(arq);

  int max_iter = 100000*size;
  float solucao[size];
  for(int i = 0; i < max_iter; i++){
      int sol_size = (rand() % (size))+1;

      for(int j = 0; j < sol_size; j++){
        solucao[j] = -1;
      }

      int entrada = 0;
      total_it = 0;
      while(entrada < sol_size){
          int index = rand() % size;
          for(int j = 0; j < sol_size; j++){

            if(solucao[j] == valor[index]){
              break;
            }

            if(solucao[j] == -1){
              solucao[entrada] = valor[index];
              entrada = entrada +1;
              total_it += valor[index];
              break;
            }
          //fim do for
          }
          if(total_it >= total){
            break;
          }
      //fim do while
      }

      if(total_it == total){
        for(int j = 0; j < sol_size; j++){
          if(solucao[j] != -1){
            printf("%.2f; ", solucao[j]);
          }
        }
        break;
      }

  }

  return 0;
}
