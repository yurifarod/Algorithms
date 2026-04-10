
import java.util.Queue;
import java.util.LinkedList;

public class UsandoCollections {

    public static void main(String[] args) {

        Queue<String> nomes = new LinkedList<>();
        nomes.add("Ana");
        nomes.add("Carlos");
        nomes.add("Mauricio");
        nomes.add("Maria");
        nomes.add("Ana");

        nomes.poll();
        nomes.poll();

        for (String nome : nomes) {
            System.out.println(nome);
        }
    }
}

