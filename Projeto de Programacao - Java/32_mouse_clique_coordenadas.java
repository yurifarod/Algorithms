/*
 * Desafio! Tome essa imagem como base e monte um jogo da velha!
 * O usuário (X) deve jogar contra o computador (O)
 * As jogadas do computador devem ter um mínimo de lógica coerente (não meramente aleatórias)
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.net.URL;

public class TelaComImagem extends JFrame {
    
    private JLabel labelImagem;

    public TelaComImagem() {
        setTitle("Captura de Mouse");
        setSize(500, 500);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Centraliza na tela

        ImageIcon imagem = new ImageIcon("C:\\Users\\Sergipetec\\Desktop\\Docente\\Projeto de Programação\\Code\\img\\imagem_0001.jpg");
        // Redimensionando a imagem
        Image imagemRedimensionada = imagem.getImage().getScaledInstance(500,500,Image.SCALE_SMOOTH);

        ImageIcon imagemFinal = new ImageIcon(imagemRedimensionada);

        // JLabel para exibir a imagem
        labelImagem = new JLabel(imagemFinal);

        // Centralizar imagem
        labelImagem.setHorizontalAlignment(JLabel.CENTER);

        add(labelImagem);

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                System.out.println(
                    "Clique em X = " + e.getX() +
                    " | Y = " + e.getY()
                );
            }
        });

        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TelaComImagem::new);
    }
}