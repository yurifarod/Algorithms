import javax.swing.*;

public class ExemploPanel {

    public static void main(String[] args) {

        JFrame janela = new JFrame("JPanel");

        JPanel painel = new JPanel();

        painel.add(new JButton("Salvar"));
        painel.add(new JButton("Cancelar"));

        janela.add(painel);

        janela.setSize(300, 200);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }
}