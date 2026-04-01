package pkg_abstract;

public abstract class Funcionario{
	
	protected String nome;

    public Funcionario(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return this.nome;
    }

    //Pq n double?
    public abstract float pagamento();
}