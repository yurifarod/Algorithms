package main.webapp;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/delete")
public class DeleteServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        // Recebendo parâmetros do formulário
        String str_codigo = request.getParameter("codigo");
        int codigo = Integer.parseInt(str_codigo);
        
        ProdutoDAO produtoDAO = new ProdutoDAO();
        int linhas = produtoDAO.deleteProduto(codigo);        
        
        out.println("<html><body>");
        if (linhas > 0) {
            out.println("<h3>Produto deletado com sucesso!</h3>");
        } else {
            out.println("<h3>Erro ao deletar produto.</h3>");
        }

        out.println("<a href='index.html'>Voltar</a>");
        out.println("</body></html>");
        
       
    }
}