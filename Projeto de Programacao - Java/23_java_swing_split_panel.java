import javax.swing.*;

public class ExemploSplit {

    public static void main(String[] args) {

        JFrame janela = new JFrame("JSplitPane");

        JTextArea esquerda = new JTextArea("Menu");
        JTextArea direita = new JTextArea("Conteúdo");

        JSplitPane split = new JSplitPane(
                JSplitPane.HORIZONTAL_SPLIT,
                esquerda,
                direita
        );

        janela.add(split);

        janela.setSize(500, 300);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }
}