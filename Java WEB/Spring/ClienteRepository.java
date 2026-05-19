package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import com.example.demo.model.Cliente;
import jakarta.transaction.Transactional;

public interface ClienteRepository extends JpaRepository<Cliente, Long> {

	@Transactional
	@Modifying
	void deleteByCpf(String cpf);
}
