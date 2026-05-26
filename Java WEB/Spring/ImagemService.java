package com.example.demo.service;

import com.example.demo.entity.Imagem;
import com.example.demo.repository.ImagemRepository;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Service
public class ImagemService {

    @Value("${upload.dir}")
    private String uploadDir;

    private final ImagemRepository repository;

    public ImagemService(ImagemRepository repository) {
        this.repository = repository;
    }

    public void salvar(MultipartFile arquivo)
            throws IOException {

        // cria pasta caso não exista
        File diretorio = new File(uploadDir);

        if (!diretorio.exists()) {
            diretorio.mkdirs();
        }

        // nome do arquivo
        String nomeArquivo = arquivo.getOriginalFilename();

        // caminho final
        Path caminho = Paths.get(uploadDir, nomeArquivo);

        // salva no diretório
        Files.write(caminho, arquivo.getBytes());

     // salva no banco
        Imagem imagem = new Imagem(
                nomeArquivo,
                arquivo.getContentType(),
                arquivo.getSize(),
                caminho.toString(),
                arquivo.getBytes()
        );
        
        repository.save(imagem);
    }
}