package Web;


import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "Hello", urlPatterns = {"/Hello"})
public class Hello extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");

        PrintWriter out = response.getWriter();
        out.println("<head>");
        out.println("<title>Hello</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h1>Olá, mundo!</h1>");
        for(int i = 0; i < 10; i++) {
        	out.println(i);
        }
        out.println("</body>");
    }
}