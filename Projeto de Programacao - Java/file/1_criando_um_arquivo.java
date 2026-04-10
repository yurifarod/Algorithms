

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class ManipulacaoArquivo {
    public static void main(String[] args) {

        try {
        	// Criando Pasta
	    	File pasta = new File("persist");
			pasta.mkdir();   // cria uma pasta
            // 1. Criando o objeto File
	        File arquivo = new File("persist/arquivo.txt");

            // 2. Criando o arquivo fisicamente
            if (arquivo.createNewFile()) {
                System.out.println("Arquivo criado com sucesso!");
            }
            else {
                System.out.println("Arquivo já existe!");
            }

            // 3. Verificando se o arquivo existe
            if (arquivo.exists()) {
                System.out.println("Confirmação: o arquivo existe.");
            }

            // 4. Escrevendo no arquivo (com fechamento automático)
            FileWriter writer = new FileWriter(arquivo);
            writer.write("Olá mundo");
            writer.close(); // fechando o recurso IMPORTANTE!

            System.out.println("Conteúdo escrito com sucesso!");

        }
        catch (IOException e) {
            System.out.println("Erro ao manipular o arquivo.");
            e.printStackTrace();
        }
    }
}

