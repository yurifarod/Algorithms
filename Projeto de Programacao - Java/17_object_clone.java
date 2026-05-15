class Produto implements Cloneable{
	String nome;

	Produto(String nome){
		this.nome = nome;
	}

	public static void main(String[] args) {
    	Produto p1 = new Produto("Café");
    	Produto p2 = null;
        Produto p3 = p1;

        try{
            p2 = (Produto) p1.clone();
    	}
        catch(CloneNotSupportedException e){
            e.printStackTrace();
        }

    	System.out.println(p1.equals(p2));
        System.out.println(p1.nome);
        System.out.println(p2.nome);
        p3.nome = "Cafezinho";
        System.out.println(p1.nome);
    }

}

