package main.webapp;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/insert")
public class InsertServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        // Recebendo parâmetros do formulário
        String nome = request.getParameter("nome");
        String categoria = request.getParameter("categoria");
        String valorStr = request.getParameter("valor");
        double valor = Double.parseDouble(valorStr);
        
        ProdutoDAO produtoDAO = new ProdutoDAO();
        
        int linhas = produtoDAO.insertProduto(nome, categoria, valor);
        
        
        out.println("<html><body>");
        if (linhas > 0) {
            out.println("<h3>Produto cadastrado com sucesso!</h3>");
        } else {
            out.println("<h3>Erro ao cadastrar produto.</h3>");
        }

        out.println("<a href='index.html'>Voltar</a>");
        out.println("</body></html>");
    }
}