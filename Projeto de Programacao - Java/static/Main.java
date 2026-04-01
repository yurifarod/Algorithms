public class Main{
    public static void main(String[] args) {
    	int resultado = Calculadora.somar(5, 3);

    	System.out.println(resultado);

    	Funcionario f1 = new Funcionario("Jorge");
    	Funcionario f2 = new Funcionario("Maria");
    	Funcionario f3 = new Funcionario("Antônia");
    	Funcionario f4 = new Funcionario("Cleide");

    	System.out.println(f4.getContador());

    	if(Empresa.validarSalario(1280)){
    		System.out.println("Válido!");

    	}
    	else{
    		System.out.println("Inválido!");    		
    	}
    }

}