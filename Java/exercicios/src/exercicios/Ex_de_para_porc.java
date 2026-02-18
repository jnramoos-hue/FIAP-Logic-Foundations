package exercicios;
import java.util.Scanner;
public class Ex_de_para_porc {

	public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            double valor, perc, acresc, desc, porc;

            // -Ler o valor
            System.out.print("Digite o valor: ");
            valor = entrada.nextDouble();

            // -Ler a porcentagem
            System.out.print("Digite a porcentagem: ");
            porc = entrada.nextDouble();

            // -Calcular o percentual
            perc = valor * porc / 100;

            // -Calcular o acréscimo
            acresc = valor + perc;

            // -Calcular o desconto
            desc = valor - perc;

            // -Exibir o percentual
            System.out.println("Percentual: " + perc);

            // -Exibir o Acréscimo
            System.out.println("Acréscimo: " + acresc);

            // -Exibir o desconto
            System.out.println("Desconto: " + desc);
        }
        // O Scanner 'entrada' é fechado automaticamente aqui
    }	
		
}

		
	

