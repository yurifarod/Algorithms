package pkg_abstract;

public class Main{
	public static void main(String[] args) {
		Professor p = new Professor("Yuri", 11);

		for(int i = 0; i < 20; i++){
			p.addHora();			
		}

		Administrativo a = new Administrativo("Jorge", 2500);

		for(int i = 0; i < 5; i++){
			a.addHora();			
		}

		System.out.println(p.getNome());
		System.out.println("Pagamento: R$ " + p.pagamento());
		System.out.println(a.getNome());
		System.out.println("Pagamento: R$ " + a.pagamento());

	}
}