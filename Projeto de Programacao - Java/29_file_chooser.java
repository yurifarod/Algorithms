import javax.swing.*;
import java.awt.event.*;
import java.io.File;

public class UploadArquivo extends JFrame {

    private JButton botaoSelecionar;
    private JLabel labelArquivo;

    public UploadArquivo() {

        setTitle("Upload de Arquivo");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(null);

        botaoSelecionar = new JButton("Selecionar Arquivo");
        //x, y (pontos), largura, altura
        botaoSelecionar.setBounds(100, 40, 180, 40);

        labelArquivo = new JLabel("Nenhum arquivo selecionado");
        labelArquivo.setBounds(30, 100, 340, 30);

        add(botaoSelecionar);
        add(labelArquivo);

        botaoSelecionar.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                JFileChooser seletor = new JFileChooser("C:\\Users\\Sergipetec\\Desktop");

                int resultado = seletor.showOpenDialog(null);

                if(resultado == JFileChooser.APPROVE_OPTION) {

                    File arquivo = seletor.getSelectedFile();

                    labelArquivo.setText("Arquivo Selecionado: " + arquivo.getAbsolutePath());
                }
            }
        });
    }

    public static void main(String[] args) {

        SwingUtilities.invokeLater(() -> {new UploadArquivo().setVisible(true);});
    }
}