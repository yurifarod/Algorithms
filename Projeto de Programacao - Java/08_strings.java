public class Main {
    public static void main(String[] args) {

    	String nome_1 = "Maria";
    	String nome_2 = new String("Maria");
    	
		if(nome_1 == nome_2){
			System.out.println("Iguais");
		}
		else if(nome_1.equals(nome_2)){
			System.out.println("Iguais, mas diferentes!");
		}
		else{
			System.out.println("Totalmente diferentes!");			
		}

		String nome_3 = "Maria";

		if(nome_1 == nome_3){
			System.out.println("Iguais agora?");
		}

    	/*String nome = "Ana";
		nome = nome + " Silva";
		System.out.println(nome);*/
    }
}

