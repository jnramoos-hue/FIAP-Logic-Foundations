package exercicios;
import java.util.Scanner;
public class Ex_de_para {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int num, mult, volta;
		
		System.out.println("Digite um número: ");
		num = teclado.nextInt();
		
		volta = 1;
		
		while(volta <= 10) {
			mult = num * volta;
			System.out.println(mult);
			volta++;
			
			
		}
		
		

	}

}
