public class Empregado {
    private String nome;
    private String cargo;
    private double valorHoraTrabalhada;
    private int horasTrabalhadas;
    private double salario;

    public Empregado(String nome, String cargo, double valorHoraTrabalhada) {
        this.nome = nome;
        this.cargo = cargo;
        this.valorHoraTrabalhada = valorHoraTrabalhada;
        this.horasTrabalhadas = 0;
        this.salario = 0.0;
    }

    // Método para incrementar a hora
    public void incrementarHoraTrabalhada() {
        this.horasTrabalhadas += 1;
    }

    // Método para calcular o salário e exibir
    public void calcularSalario() {
        this.salario = this.horasTrabalhadas * this.valorHoraTrabalhada;
        // Usamos printf para formatar as casas decimais, assim como no seu exemplo
        System.out.printf("Salario do funcionario: R$ %.2f%n", this.salario);
    }

    public static void main(String[] args) {
        Empregado empregado = new Empregado("Jorge", "Programador", 100.0);

        empregado.incrementarHoraTrabalhada();
        empregado.incrementarHoraTrabalhada();
        empregado.incrementarHoraTrabalhada();

        empregado.calcularSalario();
    }
}


