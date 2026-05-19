package com.example.demo.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Column;

@Entity
public class Cliente {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;
    
    @Column(unique = true)
    private String cpf;

    // getters e setters
    
    public String getCpf() {
		return cpf;
	}
    
    public String getNome() {
		return nome;
	}
    
    public void setCpf(String cpf) {
		this.cpf = cpf;
	}
    
    public void setNome(String nome) {
		this.nome = nome;
	}
}