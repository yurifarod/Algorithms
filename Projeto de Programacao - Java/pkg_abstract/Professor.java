package pkg_abstract;

public class Professor extends Funcionario{
	private float vl_hora;
	private byte qt_hora;

	public Professor(String nome, float vl_hora){
		super(nome);
		this.qt_hora = 0;
		this.vl_hora = vl_hora;
	}

	public void addHora(){
		this.qt_hora++;
	}

	@Override
	public float pagamento(){
		return this.vl_hora * this.qt_hora;
	}

}