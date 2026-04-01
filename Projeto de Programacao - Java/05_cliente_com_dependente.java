class Dependente {

    Cliente cliente;
    String nome;
    double limite;
    // Construtor
    public Dependente(Cliente cliente, String nome, double limite) {
        this.cliente = cliente;
        this.nome = nome;
        this.limite = limite;
    }
    // Método debitar
    public void debitar(double valor) {

        if ((cliente.saldo - valor) < cliente.chequeEspecial) {
            System.out.println("Operação negada! Consulte o seu gerente!");
        } 
        else if (valor > limite) {
            System.out.println("Limite de transação superior ao limite do dependente!");
        } 
        else {
            cliente.debitar(valor);
        }
    }
}
class Cliente {
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
    // Debitar
    public void debitar(double valor) {

        if ((saldo - valor) < chequeEspecial) {
            System.out.println("Operação negada! Consulte o seu gerente!");
        } else {
            saldo -= valor;
        }

    }
    // Creditar
    public void creditar(double valor) {
        saldo += valor;
    }
    // Consultar
    public void consultar() {
        System.out.printf("O cliente %s, possui em sua conta %s: R$ %.2f%n",
                nome, tipoConta, saldo);
    }
    // Criar dependente
    public Dependente incluirDependente(String nome, double limite) {
        Dependente dependente = new Dependente(this, nome, limite);
        return dependente;
    }
}
public class Main {
    public static void main(String[] args) {
        Cliente instanciaCliente = new Cliente("Maria de Souza", "Poupança", 1000);
        Dependente instanciaDependente =
                instanciaCliente.incluirDependente("Joao de Souza", 200);
        instanciaDependente.debitar(250);
        for (int i = 0; i < 15; i++) {
            instanciaDependente.debitar(100);
        }
        instanciaCliente.consultar();
    }
}