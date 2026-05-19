# CRUD de Produtos com Spring Boot

Este projeto consiste na migração de uma aplicação Java Web tradicional baseada em **Servlets + JSP + JDBC** para uma arquitetura moderna utilizando **Spring Boot MVC**.

O objetivo principal do projeto é didático, demonstrando a evolução entre:

- Servlets
- MVC
- Controllers
- Templates HTML
- Organização em camadas
- Integração backend/frontend

---

# Tecnologias Utilizadas

- Java
- Spring Boot
- Spring MVC
- Thymeleaf
- Maven
- HTML/CSS

---

# Arquitetura do Projeto

O projeto segue o padrão MVC (Model-View-Controller).

## Estrutura Hierárquica

```text
src/main/java
└── com.example.demo
    ├── ProdutoSpringApplication.java
    │
    ├── controller
    │   ├── ClienteController.java
    │   ├── ProdutoController.java
    │   └── ProdutoRestController.java
    │
    ├── dao
    │   └── ProdutoDAO.java
    │
    ├── entity
    │   └── Produto.java
    │
    ├── model
    │   └── Cliente.java
    │
    └── repository
        └── ClienteRepository.java

src/main/resources
├── templates
│   ├── delete.html
│   ├── erro.html
│   ├── form.html
│   ├── index.html
│   ├── list.html
│   └── success.html
│
└── application.properties

Arquivos principais
├── pom.xml
