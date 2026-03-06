import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      char vet[];

      for(int i = 0; i < 5; i++){
        System.out.println("Digite um caractere");
        char c = sc.next().charAt(0);
      }
      
      sc.close();
    }
}

