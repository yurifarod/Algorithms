import javax.swing.JFrame;
import javax.swing.JLabel;

public class JanelaSimples {

    public static void main(String[] args) {

        JFrame janela = new JFrame("Minha Primeira Janela");

        JLabel texto = new JLabel("Olá, Swing!");

        janela.add(texto);

        janela.setSize(300, 200);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }
}