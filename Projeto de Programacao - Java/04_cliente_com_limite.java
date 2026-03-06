public class Cliente {
    String nome;
    String tipoConta;
    double saldo;
    double chequeEspecial;
    // Construtor
    public Cliente(String nome, String tipoConta, double depositoInicial) {
        this.nome = nome;
        this.tipoConta = tipoConta;
        this.saldo = depositoInicial;
        this.chequeEspecial = -100;
    }
    // Método debitar com verificação de limite
    public void debitar(double valor) {

        if ((saldo - valor) < chequeEspecial) {
            System.out.println("Operação negada! Consulte o seu gerente!");
        } else {
            saldo -= valor;
        }

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

    // Método principal
    public static void main(String[] args) {
        Cliente instanciaCliente = new Cliente("Maria de Souza", "Poupança", 1000);
        instanciaCliente.debitar(100);
        instanciaCliente.debitar(800);
        instanciaCliente.debitar(135.76);
        instanciaCliente.consultar();
        instanciaCliente.debitar(70);
    }
}