
import java.util.Map;
import java.util.HashMap;

public class UsandoCollections {

    public static void main(String[] args) {

        Map<Integer, String> nomes = new HashMap<>();
        nomes.put(101, "Ana");
        nomes.put(245, "Carlos");
        nomes.put(112, "Mauricio");
        nomes.put(111, "Maria");
        nomes.put(1, "Ana");

        int[] ids = {1, 101, 111, 112, 245, 3001};

        for (int id : ids) {
            System.out.println(nomes.get(id));
        }
    }
}

