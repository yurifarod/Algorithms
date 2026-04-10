
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.List;

public class LerArquivo {
    public static void main(String[] args) {

        try {
            List<String> linhas = Files.readAllLines(Paths.get("persist/arquivo.txt"));

            for (String linha : linhas) {
                System.out.println(linha);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

