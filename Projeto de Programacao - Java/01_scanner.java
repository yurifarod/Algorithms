import java.util.Scanner;

public class CadastroUsuario {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite seu nome:");
        String nome = sc.nextLine();

        System.out.println("Digite sua idade:");
        int idade = sc.nextInt();

        System.out.println("Digite sua altura (ex: 1.75):");
        double altura = sc.nextDouble();

        System.out.println("Digite seu peso (ex: 70.5):");
        double peso = sc.nextDouble();

        System.out.println("Você se chama: " + nome);
        System.out.println("Idade: " + idade + " anos");
        System.out.println("Altura: " + altura + " m");
        System.out.println("Peso: " + peso + " kg");

        sc.close();
    }
}