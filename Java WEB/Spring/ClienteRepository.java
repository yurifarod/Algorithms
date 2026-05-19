package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.demo.model.Cliente;

public interface ClienteRepository extends JpaRepository<Cliente, Long> {
	
	void deleteByCpf(String cpf);
}