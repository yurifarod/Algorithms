
import java.util.List;
import java.util.ArrayList;

public class UsandoCollections {

    public static void main(String[] args) {

        List<String> nomes = new ArrayList<>();
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

