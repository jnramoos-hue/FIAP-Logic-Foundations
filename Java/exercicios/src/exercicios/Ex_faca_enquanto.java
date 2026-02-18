package exercicios;
import java.util.Scanner;
public class Ex_faca_enquanto {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		// Declaração das variáveis
		int num, mult, volta;
		
		System.out.println("Digite um número: ");
		num = teclado.nextInt();
		
		volta = 1;
		
		do {
			mult = num * volta;
			System.out.println(mult);
			volta++;
		}while(volta <= 10);

	}

}
