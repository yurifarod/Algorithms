package com.example.demo.repository;

import com.example.demo.entity.Imagem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ImagemRepository
        extends JpaRepository<Imagem, Long> {
}