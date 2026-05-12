# CRUD Java Web com Servlet, DAO e PostgreSQL

## Descrição

Este projeto consiste em uma aplicação Java Web simples de CRUD (Create, Read, Update e Delete) utilizando:

- Java Servlet
- PostgreSQL
- JDBC
- DAO (Data Access Object)
- HTML
- Apache Tomcat

O sistema permite o cadastro, consulta e remoção de produtos armazenados em banco de dados PostgreSQL.

---

## Estrutura do Projeto

```text
src/
 ├── model/
 │    └── Produto.java
 │
 ├── dao/
 │    └── ProdutoDAO.java
 │
 ├── servlet/
 │    ├── CadastroServlet.java
 │    ├── ConsultaServlet.java
 │    └── DeleteServlet.java
 │
WebContent/
 ├── index.html
 ├── cadastro.html
 ├── delete.html
 └── consulta.html