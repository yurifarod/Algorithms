class Veiculo {
    String marca;
    String modelo;
    String placa;
    // Construtor
    public Veiculo(String marca, String modelo, String placa) {
        this.marca = marca;
        this.modelo = modelo;
        this.placa = placa;
    }
    public void imprimir() {
        System.out.println("Seu veículo é um " + marca + ", " + modelo + ", com placa: " + placa);
    }
}
class Carro extends Veiculo {
    int portas;
    // Construtor
    public Carro(String marca, String modelo, String placa, int portas) {
        super(marca, modelo, placa); // chama o construtor da classe pai
        this.portas = portas;
    }
    // Sobrescrita de método
    @Override
    public void imprimir() {
        System.out.println("Seu carro é um " + marca + ", " + modelo + ", "
                + portas + " portas, com placa: " + placa);
    }
}
public class Main {
    public static void main(String[] args) {
        Veiculo v = new Veiculo("Ford", "Ka", "HZY1234");
        v.imprimir();
        Carro c = new Carro("Renault", "Kwid", "HZY1235", 3);
        c.imprimir();
    }
}