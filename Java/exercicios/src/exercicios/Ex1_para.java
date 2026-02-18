package exercicios;
import java.util.Scanner;
public class Ex1_para {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int num, mult, volta;
		
		System.out.println("Digite um número: ");
		num = teclado.nextInt();
		
		for (volta = 1; volta <= 10; volta++) {
			mult = num * volta;
			System.out.println(mult);
		}

	}

}
