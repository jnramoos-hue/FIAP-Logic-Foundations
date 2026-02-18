package exercicios;
import java.util.Scanner;
public class Ex_enquanto_faca {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		//Declaração de variáveis
		float  num = 1, soma = 0;
		
		System.out.println("Digite 0 para finalizar: ");
		
		while(num != 0 ) {
			System.out.println("Digite um numero: ");
			num = teclado.nextFloat();
			soma += num; // equivale à soma = soma + 1
		}
		
		// Exibe a somatória 
		System.out.println("Somatória = " + soma);
		

	}

}
