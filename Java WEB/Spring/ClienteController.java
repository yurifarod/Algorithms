package com.example.demo.controller;

import java.util.List;

import com.example.demo.model.Cliente;
import com.example.demo.repository.ClienteRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/clientes")
public class ClienteController {

    @Autowired
    private ClienteRepository repository;

    @GetMapping("/inserir/{nome}/{cpf}")
    public Cliente criar(
            @PathVariable String nome,
            @PathVariable String cpf) {

        Cliente cliente = new Cliente();
        cliente.setNome(nome);
        cliente.setCpf(cpf);

        return repository.save(cliente);
    }

    @GetMapping("/cpf/{cpf}")
    public void deletarPorCpf(@PathVariable String cpf) {
        repository.deleteByCpf(cpf);
    }
    
    @GetMapping
    public List<Cliente> listarTodos() {
        return repository.findAll();
    }
}
