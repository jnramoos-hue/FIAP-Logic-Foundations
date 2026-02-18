package exercicios;
import java.util.Scanner;
public class Ex2_faca_enquanto {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		// Declaração das variáveis
		int n, fat;
		
		System.out.println("Digite um número: ");
		n = teclado.nextInt();
		
		fat = 1;
		
		do {
			fat *= n;
			n--;
			
		}while(n > 1);
		
		System.out.println("Fatorial = " + fat);

	}

}
