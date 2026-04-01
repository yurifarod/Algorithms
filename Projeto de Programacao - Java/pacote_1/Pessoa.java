package pacote_1;

public class Pessoa{
	
	String nome;

	Pessoa(String nome) {
        this.nome = nome;
    }

    String getPessoa(){
    	return this.nome;
    }

    void setPessoa(String nome){
    	this.nome = nome;
    }
}