package exercicios;
import java.util.Scanner;
public class Intro {
	
	public static void main(String[] args) {
	try	(Scanner entrada = new Scanner(System.in)){
		int n1, n2, soma;
		
		//ler n1
		System.out.print("Digite um numero: ");
		n1 = entrada.nextInt();
		
		//ler n2 
		System.out.print("Digite outro numero: ");
		n2 = entrada.nextInt();
		
		//soma = n1 + n2
		soma = n1 + n2;
				
		//Escreva soma
		System.out.print("Soma = " + soma);

		}
	

	}

}
