package main.webapp;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/consulta")
public class ConsultaServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><body>");
        out.println("<h2>Lista de Produtos</h2>");
        
        ProdutoDAO produtoDAO = new ProdutoDAO();
        Produto[] produtos = produtoDAO.consultaProdutos();

        out.println("<table border='1'>");
        out.println("<tr><th>Nome</th><th>Categoria</th><th>Valor</th></tr>");

        for(Produto p : produtos) {
            out.println("<tr>");
            out.println("<td>" + p.getNome() + "</td>");
            out.println("<td>" + p.getCategoria() + "</td>");
            out.println("<td>" + String.valueOf(p.getValor()) + "</td>");
            out.println("</tr>");
        
        }
        out.println("</table>");
        out.println("<br><a href='index.html'>Voltar</a>");
        out.println("</body></html>");
    }
}