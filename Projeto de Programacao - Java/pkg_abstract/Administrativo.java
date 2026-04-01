package pkg_abstract;

public class Administrativo extends Funcionario{
	private float salario;

	public Administrativo(String nome, float salario){
		super(nome);
		this.salario = salario;
	}

	public void addHora(){
		this.salario += (this.salario/220)*1.5;
	}

	@Override
	public float pagamento(){
		return this.salario;
	}

}