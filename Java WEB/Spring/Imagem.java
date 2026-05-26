package com.example.demo.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "tb_imagem")
public class Imagem {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nomeArquivo;

    private String tipoArquivo;

    private Long tamanho;

    private String caminho;
    
    @Lob
    private byte[] dados;

    public Imagem() {
    }

    public Imagem(String nomeArquivo,
                  String tipoArquivo,
                  Long tamanho,
                  String caminho,
                  byte[] dados) {

        this.nomeArquivo = nomeArquivo;
        this.tipoArquivo = tipoArquivo;
        this.tamanho = tamanho;
        this.caminho = caminho;
        this.dados = dados;
    }

    // GETTERS E SETTERS
}