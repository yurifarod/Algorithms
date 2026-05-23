import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CalculadoraSwing extends JFrame {

    private JTextField campoNumero1;
    private JTextField campoNumero2;

    private JRadioButton radioSoma;
    private JRadioButton radioSubtracao;

    private boolean preenchendoPrimeiro = true;

    public CalculadoraSwing() {

        setTitle("Calculadora Swing");

        setSize(400, 500);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setLayout(new BorderLayout());

        // =========================
        // PAINEL SUPERIOR
        // =========================

        JPanel painelTopo = new JPanel();

        painelTopo.setLayout(new GridLayout(4, 1));

        campoNumero1 = new JTextField();
        campoNumero2 = new JTextField();

        campoNumero1.setEditable(false);
        campoNumero2.setEditable(false);

        painelTopo.add(new JLabel("Primeiro número:"));
        painelTopo.add(campoNumero1);

        painelTopo.add(new JLabel("Segundo número:"));
        painelTopo.add(campoNumero2);

        add(painelTopo, BorderLayout.NORTH);

        // =========================
        // PAINEL CENTRAL (BOTÕES)
        // =========================

        JPanel painelNumeros = new JPanel();

        painelNumeros.setLayout(new GridLayout(4, 3, 5, 5));

        for (int i = 1; i <= 9; i++) {

            JButton botao = new JButton(String.valueOf(i));

            botao.addActionListener(new ActionListener() {

                @Override
                public void actionPerformed(ActionEvent e) {

                    adicionarNumero(botao.getText());
                }
            });

            painelNumeros.add(botao);
        }

        // Botão 0
        JButton botaoZero = new JButton("0");

        botaoZero.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                adicionarNumero("0");
            }
        });

        painelNumeros.add(new JLabel());
        painelNumeros.add(botaoZero);
        painelNumeros.add(new JLabel());

        add(painelNumeros, BorderLayout.CENTER);

        // =========================
        // PAINEL INFERIOR
        // =========================

        JPanel painelInferior = new JPanel();

        painelInferior.setLayout(new GridLayout(3, 1));

        // Radio Buttons
        radioSoma = new JRadioButton("Soma");
        radioSubtracao = new JRadioButton("Subtração");

        ButtonGroup grupo = new ButtonGroup();

        grupo.add(radioSoma);
        grupo.add(radioSubtracao);

        radioSoma.setSelected(true);

        JPanel painelOperacoes = new JPanel();

        painelOperacoes.add(radioSoma);
        painelOperacoes.add(radioSubtracao);

        painelInferior.add(painelOperacoes);

        // Botão trocar campo
        JButton botaoTrocar = new JButton("Trocar Número");

        botaoTrocar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(preenchendoPrimeiro){
                    preenchendoPrimeiro = false;
                }
                else{
                    preenchendoPrimeiro = true;
                }
            }
        });

        painelInferior.add(botaoTrocar);

        // Botão calcular
        JButton botaoCalcular = new JButton("Calcular");

        botaoCalcular.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                calcular();
            }
        });

        painelInferior.add(botaoCalcular);

        add(painelInferior, BorderLayout.SOUTH);

        setVisible(true);
    }

    // =========================
    // MÉTODO PARA ADICIONAR NÚMEROS
    // =========================

    private void adicionarNumero(String numero) {
        if (preenchendoPrimeiro) {

            campoNumero1.setText(campoNumero1.getText() + numero);
        }
        else{
            campoNumero2.setText(campoNumero2.getText() + numero);
        }
    }

    // =========================
    // MÉTODO CALCULAR
    // =========================

    private void calcular() {

        try {int numero1 = Integer.parseInt(campoNumero1.getText());
            int numero2 = Integer.parseInt(campoNumero2.getText());
            int resultado;

            if (radioSoma.isSelected()) {
                resultado = numero1 + numero2;
            }
            else{
                resultado = numero1 - numero2;
            }
            JOptionPane.showMessageDialog(null,"Resultado: " + resultado);
            campoNumero1.setText("");
            campoNumero2.setText("");

        }
        catch (Exception e) {
            JOptionPane.showMessageDialog(null,"Preencha os números corretamente!");
        }
    }

    // =========================
    // MAIN
    // =========================

    public static void main(String[] args) {

        new CalculadoraSwing();
    }
}