

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class EscreverMaisLinhas {
    public static void main(String[] args) {

        try {
            // 1. Referência ao arquivo
            File arquivo = new File("persist/arquivo.txt");

            // 2. Verifica se existe antes de escrever
            if (!arquivo.exists()) {
                System.out.println("Arquivo não existe!");
                return;
            }

            // 3. Abre o arquivo no modo APPEND (true)
            try (FileWriter writer = new FileWriter(arquivo, true)) {

                writer.write("\nNova linha 1");
                writer.write("\nNova linha 2");
                writer.write("\nNova linha 3");

                System.out.println("Linhas adicionadas com sucesso!");
            }

        } catch (IOException e) {
            System.out.println("Erro ao escrever no arquivo.");
            e.printStackTrace();
        }
    }
}

