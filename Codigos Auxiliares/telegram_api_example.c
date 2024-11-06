#include <windows.h>
#include <stdio.h>

int main(){
	
	char retorno[] = "curl -I \"https://api.telegram.org/botSEU_TOKEN/sendmessage?chat_id=SEU_id&text=Pressao:%d;Temperatura%d";
	int pressao = 41;
	int temperatura = 74;

	sprintf(retorno, retorno, pressao, temperatura);

	system(retorno);

	return 0;
}