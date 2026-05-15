class Medicamento {
    private String nome;
    private double timer;
    private int qtd;
    
    public Medicamento(String nome, double timer, int qtd) {
        this.nome = nome;
        this.timer = timer;
        this.qtd = qtd;
    }

    public void iniciarMedicacao() {
        for(int i = 0; i < qtd; i++) {

            try {

                Thread.sleep((long)(timer * 1000));

            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("Tomando a dose " + (i + 1)+ " do medicamento "+ nome);
        }
    }

    public static void main(String[] args) {
        Medicamento remedio1 = new Medicamento("Paracetamol", 0.3, 5);
        Medicamento remedio2 = new Medicamento("Ibuprofeno", 0.5, 5);
        remedio1.iniciarMedicacao();
        remedio2.iniciarMedicacao();
    }
}

