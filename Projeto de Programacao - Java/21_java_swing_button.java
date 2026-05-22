import javax.swing.*;
import java.awt.event.*;

public class ExemploBotao {

    public static void main(String[] args) {

        JFrame janela = new JFrame("Evento");

        JButton botao = new JButton("Clique aqui");

        botao.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Botão clicado!");
            }
        });

        janela.add(botao);

        janela.setSize(300, 200);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setVisible(true);
    }
}

