package main.webapp;

public class Produto {
    private int id;
    private String nome;
    private String categoria;
    private double valor;

    public Produto(int id, String nome, String categoria, double valor) {
        this.id = id;
        this.nome = nome;
        this.categoria = categoria;
        this.valor = valor;
    }
    
    // Getters
    public String getNome() { return nome; }
    public String getCategoria() { return categoria; }
    public double getValor() { return valor; }
}