import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

public class CopiarImagem extends JFrame {

    private JButton botaoSelecionar;

    public CopiarImagem() {

        setTitle("Copiar Imagem");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(null);

        botaoSelecionar = new JButton("Selecionar Imagem");
        botaoSelecionar.setBounds(100, 60, 180, 40);

        add(botaoSelecionar);

        botaoSelecionar.addActionListener(e -> selecionarECopiarImagem());
    }

    private void selecionarECopiarImagem() {

        JFileChooser seletor = new JFileChooser("C:\\upload");

        // Filtrar apenas imagens
        FileNameExtensionFilter filtro = new FileNameExtensionFilter("Imagens", "jpg", "jpeg", "png", "gif");

        seletor.setFileFilter(filtro);

        int resultado = seletor.showOpenDialog(this);

        if (resultado == JFileChooser.APPROVE_OPTION) {

            File imagemSelecionada = seletor.getSelectedFile();

            // Diretório destino
            File diretorioDestino = new File("C:\\Users\\Sergipetec\\Desktop\\Docente\\Projeto de Programação\\Code\\img");

            // Cria a pasta caso não exista
            if (!diretorioDestino.exists()) {
                diretorioDestino.mkdirs();
            }

            String new_name = "imagem_0001.jpg";
            // Arquivo destino
            File arquivoDestino = new File(diretorioDestino, new_name);

            try {

                Files.copy(imagemSelecionada.toPath(),
                            arquivoDestino.toPath(),
                            StandardCopyOption.REPLACE_EXISTING);

                JOptionPane.showMessageDialog(this, "Imagem copiada com sucesso!\n\nDestino:\n"+ arquivoDestino.getAbsolutePath());
            }
            catch (IOException ex) {
                JOptionPane.showMessageDialog(this, "Erro ao copiar imagem:\n" + ex.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {new CopiarImagem().setVisible(true);});
    }
}