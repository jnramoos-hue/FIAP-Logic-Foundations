package exercicios;
import java.util.Scanner;
public class Ex3_enquanto_faca {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		//Declaração de variáveis
		int num, mult, volta;
		
		System.out.println("Digite um número: ");
		num = teclado.nextInt();
		volta = 1;
			
		while(volta <= 10) {
			mult = num * volta;
			System.out.println(num + " X " + volta + " = " + mult);
			volta++;
			
		}
		

	}

}
