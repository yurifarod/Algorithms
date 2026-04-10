
import java.util.Set;
import java.util.HashSet;

public class UsandoCollections {

    public static void main(String[] args) {

        Set<String> nomes = new HashSet<>();
        nomes.add("Ana");
        nomes.add("Carlos");
        nomes.add("Mauricio");
        nomes.add("Maria");
        nomes.add("Ana");

        for (String nome : nomes) {
            System.out.println(nome);
        }
    }
}

