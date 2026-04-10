
import java.util.*;

public class ExemploIterator {
    public static void main(String[] args) {

        List<String> nomes = new ArrayList<>();
        nomes.add("Ana");
        nomes.add("Carlos");
        nomes.add("Maria");

        Iterator<String> it = nomes.iterator();

        while (it.hasNext()) {
            String nome = it.next();
            System.out.println(nome);

            if (nome.equals("Carlos")) {
                System.out.println(nome + " foi removido");
                it.remove(); // seguro!
            }
        }
    }
}

