import javax.swing.*;
import java.awt.*;

public class MostrarImagem extends JFrame {

    private JLabel labelImagem;

    public MostrarImagem() {

        setTitle("Visualizador de Imagem");
        setSize(600, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Caminho da imagem
        ImageIcon imagem = new ImageIcon("C:\\Users\\Sergipetec\\Desktop\\Docente\\Projeto de Programação\\Code\\img\\imagem_0001.jpg");

        // Redimensionando a imagem
        Image imagemRedimensionada = imagem.getImage().getScaledInstance(500,350,Image.SCALE_SMOOTH);

        ImageIcon imagemFinal = new ImageIcon(imagemRedimensionada);

        // JLabel para exibir a imagem
        labelImagem = new JLabel(imagemFinal);

        // Centralizar imagem
        labelImagem.setHorizontalAlignment(JLabel.CENTER);

        add(labelImagem);

        setVisible(true);
    }

    public static void main(String[] args) {

        SwingUtilities.invokeLater(() -> {new MostrarImagem();});
    }
}