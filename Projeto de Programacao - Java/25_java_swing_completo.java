import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CadastroSwing {

    public static void main(String[] args) {

        JFrame janela = new JFrame("Sistema de Cadastro");

        janela.setSize(400, 300);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel painel = new JPanel();

        painel.setLayout(new GridLayout(6, 2));

        // Nome
        JLabel labelNome = new JLabel("Nome:");
        JTextField campoNome = new JTextField();

        // Email
        JLabel labelEmail = new JLabel("Email:");
        JTextField campoEmail = new JTextField();

        // Curso
        JLabel labelCurso = new JLabel("Curso:");

        String[] cursos = {"Ciência da Computação",
                            "Sistemas de Informação",
                            "Análise e Desenvolvimento de Sistemas",
                            "Direito"};

        JComboBox<String> comboCurso = new JComboBox<>(cursos);

        // Linguagem favorita
        JLabel labelJava = new JLabel("Gosta de Java?");

        JCheckBox checkJava = new JCheckBox("Sim");

        // Botão
        JButton botaoCadastrar = new JButton("Cadastrar");

        // Adicionando componentes
        painel.add(labelNome);
        painel.add(campoNome);

        painel.add(labelEmail);
        painel.add(campoEmail);

        painel.add(labelCurso);
        painel.add(comboCurso);

        painel.add(labelJava);
        painel.add(checkJava);

        painel.add(new JLabel());
        painel.add(botaoCadastrar);

        // Evento do botão
        botaoCadastrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nome = campoNome.getText();
                String email = campoEmail.getText();
                String curso = (String) comboCurso.getSelectedItem();
                boolean gostaJava = checkJava.isSelected();
                JOptionPane.showMessageDialog(null,nome+", seu cadastro feito com sucesso. No curso: "+curso);
            }
        });

        janela.add(painel);

        janela.setVisible(true);
    }
}