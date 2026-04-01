package pacote_1;

public class Main{
	public static void main(String[] args) {
		Pessoa p = new Pessoa("Jorge");
		System.out.println(p.getPessoa());

		p.setPessoa("Mauricio");
		System.out.println(p.getPessoa());

	}
}