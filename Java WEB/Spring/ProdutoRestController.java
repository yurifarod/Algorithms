package com.example.demo.controller;

import java.util.List;
import java.util. Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.dao.ProdutoDAO;
import com.example.demo.entity.Produto;

@RestController
public class ProdutoRestController {

	@Autowired
    private ProdutoDAO produtoDAO;

    @GetMapping("/api/produtos")
    public List<Produto> listarProdutos() {
    	List<Produto> produto_list = Arrays.asList(produtoDAO.consultaProdutos());
        
    	return produto_list;
    }
}