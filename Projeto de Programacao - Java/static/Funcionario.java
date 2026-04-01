public class Funcionario {

    protected String nome;
    protected int id;

    private static int contador = 0;

    public Funcionario(String nome) {
        this.nome = nome;
        this.id = ++contador;
    }

    public int getContador(){
    	return this.contador;
    }
}