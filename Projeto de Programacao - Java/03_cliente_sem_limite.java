public class Cliente {

    String nome;
    String tipoConta;
    double saldo;

    // Construtor
    public Cliente(String nome, String tipoConta, double depositoInicial) {
        this.nome = nome;
        this.tipoConta = tipoConta;
        this.saldo = depositoInicial;
    }

    // Método debitar
    public void debitar(double valor) {
        saldo -= valor;
    }

    // Método creditar
    public void creditar(double valor) {
        saldo += valor;
    }

    // Método consultar
    public void consultar() {
        System.out.printf("O cliente %s, possui em sua conta %s: R$ %.2f%n",
                nome, tipoConta, saldo);
    }

    // Método main (ponto de entrada do programa)
    public static void main(String[] args) {

        Cliente instanciaCliente = new Cliente("Maria de Souza", "Poupança", 1000);

        instanciaCliente.debitar(100);
        instanciaCliente.creditar(200);
        instanciaCliente.creditar(300);
        instanciaCliente.debitar(800);
        instanciaCliente.creditar(120);
        instanciaCliente.debitar(135.76);

        instanciaCliente.consultar();
    }
}


