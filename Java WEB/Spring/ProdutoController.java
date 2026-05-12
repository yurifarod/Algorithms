package com.example.demo.controller;

import java.io.PrintWriter;


import org.springframework.ui.Model;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo.dao.ProdutoDAO;

@Controller
public class ProdutoController {

    @Autowired
    private ProdutoDAO produtoDAO;
    
    @GetMapping("/")
    public String home() {
        return "index";
    }

    @GetMapping("/produtos")
    public String listarProdutos(Model model) {

        model.addAttribute(
                "produtos",
                produtoDAO.consultaProdutos()
        );

        return "list";
    }
    
    @GetMapping("/cadastro")
    public String abrirFormulario() {
        return "form";
    }
    
    @GetMapping("/delete")
    public String abrirDelete() {
        return "delete";
    }
    
    @GetMapping("/insert")
    public String abrirInsert(@RequestParam String nome, @RequestParam String categoria, @RequestParam Double valor) {
    	ProdutoDAO produtoDAO = new ProdutoDAO();
        
        int linhas = produtoDAO.insertProduto(nome, categoria, valor);
        if (linhas > 0) {
        	return "success";
        }
        else {
        	return "error";
        }
    }
    
    @GetMapping("/deletar")
    public String abrirInsert(@RequestParam int codigo) {
    	ProdutoDAO produtoDAO = new ProdutoDAO();
        
        int linhas = produtoDAO.deleteProduto(codigo);
        if (linhas > 0) {
        	return "success";
        }
        else {
        	return "error";
        }
    }
}