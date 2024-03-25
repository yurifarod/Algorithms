#include <stdio.h>
int main(void)
{
  char matrix[10][10];

  for(int i = 0; i < 10; i++){
  	for(int j = 0; j < 10; j++){

  		if(i == j){
  			matrix[i][j] = '#';
  		}
  		else{
  			matrix[i][j] = ' ';
  		}
  	}
  }

  for(int i = 0; i < 10; i++){
  	for(int j = 0; j < 10; j++){

  		printf("%c", matrix[i][j]);
  	}
    printf("\n");
  }
  return 0;
}