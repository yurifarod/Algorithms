import javax.swing.*;

public class ExemploScroll {

    public static void main(String[] args) {

        JFrame janela = new JFrame("JScrollPane");

        JTextArea area = new JTextArea(20, 30);

        for(int i = 1; i <= 100; i++) {
            area.append("Linha " + i + "\n");
        }

        JScrollPane scroll = new JScrollPane(area);

        janela.add(scroll);

        janela.setSize(300, 200);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }
}