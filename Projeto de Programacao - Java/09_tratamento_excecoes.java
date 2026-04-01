public class Main {
    public static void main(String[] args) {
      try {
          int x = 10 / 0;
      }
      catch (ArithmeticException e) {
          System.out.println("Não é possível dividir por zero!");
      }
      finally{
      	System.out.println("Imprime de qlqr jeito!");
      }
    }
}