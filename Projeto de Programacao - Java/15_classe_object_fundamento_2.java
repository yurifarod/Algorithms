class Produto{
	String nome;

	Produto(String nome){
		this.nome = nome;
	}

	@Override
	public String toString(){
		return "Nome do Produto: " + this.nome;
	}

    public static void main(String[] args) {
    	Produto p1 = new Produto("Café");
    	Produto p2 = new Produto("Café");

    	System.out.println(p1);
    	System.out.println(p2);
    	System.out.println(p1.equals(p2));
    }

}