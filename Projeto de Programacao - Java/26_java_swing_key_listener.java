import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ExemploKeyListener {

    public static void main(String[] args) {

        JFrame janela = new JFrame("KeyListener");

        janela.setSize(500, 400);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Campo de texto
        JTextField campoTexto = new JTextField();
        // Área de log
        JTextArea areaLog = new JTextArea();
        areaLog.setEditable(false);
        JScrollPane scroll = new JScrollPane(areaLog);
        // Painel superior
        JPanel painelTopo = new JPanel(new BorderLayout());
        painelTopo.add(new JLabel("Digite algo:"),BorderLayout.NORTH);
        painelTopo.add(campoTexto,BorderLayout.CENTER);
        // Split vertical
        JSplitPane split = new JSplitPane(JSplitPane.VERTICAL_SPLIT,painelTopo,scroll);
        // Divide meio a meio
        split.setDividerLocation(150);
        // Permite redimensionamento
        split.setResizeWeight(0.5);
        // Evento teclado
        campoTexto.addKeyListener(new KeyAdapter() {

            @Override
            public void keyPressed(KeyEvent e) {

                areaLog.append("Tecla Pressionada: "+ KeyEvent.getKeyText(e.getKeyCode())+ "\n");
            }
        });
        janela.add(split);
        janela.setVisible(true);
    }
}