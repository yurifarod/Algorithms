package com.example.demo.controller;

import com.example.demo.service.ImagemService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@Controller
@RequestMapping("/imagem")
public class ImagemController {

    private final ImagemService service;

    public ImagemController(ImagemService service) {
        this.service = service;
    }

    @GetMapping("/carregar")
    public String index() {
        return "imagem";
    }

    @PostMapping("/upload")
    public String upload(
            @RequestParam("arquivo")
            MultipartFile arquivo,
            Model model) {

        try {

            service.salvar(arquivo);

            model.addAttribute(
                    "mensagem",
                    "Upload realizado com sucesso!"
            );

        } catch (Exception e) {

            model.addAttribute(
                    "mensagem",
                    "Erro no upload!"
            );
        }

        return "imagem";
    }
}