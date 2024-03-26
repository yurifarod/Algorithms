#include <stdio.h>
int main(void)
{
  char matrix[100][100];
  int dim;

  printf("Digite as dimensoes da imagem\n");
  scanf("%d", &dim);

  for(int i = 0; i < dim; i++){
  	for(int j = 0; j < dim; j++){

  		if(i == j){
  			matrix[i][j] = '#';
  		}
  		else{
  			matrix[i][j] = ' ';
  		}
  	}
  }

  for(int i = 0; i < dim; i++){
  	for(int j = 0; j < dim; j++){

  		printf("%c", matrix[i][j]);
  	}
    printf("\n");
  }
  return 0;
}