package exercicios;
import java.util.Scanner;
public class Ex2_para {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		//Declaração das variáveis
		int n, fat, volta;
		
		System.out.println("Digite um número: ");
		n = teclado.nextInt();
		
		fat = 1;
		
		for (volta = n; volta > 1; volta--) {
			fat *= volta;
		}
		
		System.out.println("Fatorial = " + fat);

	}

}
