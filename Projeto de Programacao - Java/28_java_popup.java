import javax.swing.JOptionPane;
import java.util.Scanner;

public class Alerta{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.println("Digite seu nome: ");
		
		String nome = sc.nextLine();
		
		JOptionPane.showMessageDialog(null, nome);
	}
}