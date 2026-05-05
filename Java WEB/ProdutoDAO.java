package main.webapp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

/*
 * Fazer a classe e o DAO bonitinho, chamando tudo DAQUI!
 * */

public class ProdutoDAO {
	
	public ProdutoDAO() {
		
	}
	
	public Connection Connection(){
		try {
			Class.forName("org.postgresql.Driver");
			Connection conn = DriverManager.getConnection(
	                "jdbc:postgresql://localhost:5432/web_class",
	                "postgres",
	                "postgres"
	            );
	        
	        return conn;
		}
		catch (Exception e) {
			System.out.println("##### Erro de conexão #####");
			System.out.println(e.getMessage());
	        return null;
        }
	}
	
	public int insertProduto(String nome, String categoria, double valor){
		
		int linhas = -1;
		
		try {
			Connection conn = Connection();
			Statement query = conn.createStatement();
			
			ResultSet rs = query.executeQuery("select max(codigo)+1 as codigo from sgdb_example.tb_produto");
	        
	        int codigo = -1;
	    	while (rs.next()) {
	        	codigo = rs.getInt("codigo");
	    	}
	    	
	    	query.close();
	    	
	    	String sql = "INSERT INTO sgdb_example.tb_produto (codigo, nome, categoria, valor) VALUES (?, ?, ?, ?)";
	        PreparedStatement insert = conn.prepareStatement(sql);
	        
	        insert.setInt(1, codigo);
	        insert.setString(2, nome);
	        insert.setString(3, categoria);
	        insert.setDouble(4, valor);
	
	        linhas = insert.executeUpdate();
	        
	        insert.close();
	        conn.close();
	    	
		}
		catch (Exception e) {
			 e.printStackTrace();
        }
		return linhas;
	}
	
	public Produto[] consultaProdutos() {
		Produto[] produtos = null;
		
		try {			
			
			Connection conn = Connection();
			Statement query = conn.createStatement();
			
			ResultSet rsCount = query.executeQuery("SELECT COUNT(*) AS total FROM sgdb_example.tb_produto");
            int total = 0;

            if (rsCount.next()) {
                total = rsCount.getInt("total");
            }
            
            rsCount.close();
            
            //Cria efetivamente o Array de retorno
            produtos = new Produto[total];
            
			ResultSet rs = query.executeQuery("SELECT codigo, nome, categoria, valor FROM sgdb_example.tb_produto");
			
			int i = 0;
			while (rs.next()) {
                produtos[i] = new Produto(
                    rs.getInt("codigo"),
                    rs.getString("nome"),
                    rs.getString("categoria"),
                    rs.getDouble("valor")
                );
                i++;
            }
			
			rs.close();
			query.close();
			conn.close();
		
		}
		catch (Exception e) {
			 e.printStackTrace();
        }
		
		return produtos;
	}
	
	public int deleteProduto(int codigo) {
		int linhas = -1;
		
		try {
			Connection conn = Connection();
			String sql = "delete from sgdb_example.tb_produto where codigo = ?";
			PreparedStatement delete = conn.prepareStatement(sql);
			delete.setInt(1, codigo);
            linhas = delete.executeUpdate();
		}
		catch (Exception e) {
			 e.printStackTrace();
        }
		return linhas;
	}

}
