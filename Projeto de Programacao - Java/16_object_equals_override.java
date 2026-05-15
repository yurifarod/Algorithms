class Produto{
	String nome;

	Produto(String nome){
		this.nome = nome;
	}

	@Override
    public boolean equals(Object obj) {
        Produto outro = (Produto) obj;
        return this.nome.equals(outro.nome);
    }

    public static void main(String[] args) {
    	Produto p1 = new Produto("Café");
    	Produto p2 = new Produto("Café");
    	
    	System.out.println(p1.equals(p2));
    }

}

