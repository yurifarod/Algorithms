public class Empresa {

    public static double salarioMinimo = 1320.00;

    public static boolean validarSalario(double salario) {
        return salario >= salarioMinimo;
    }
}