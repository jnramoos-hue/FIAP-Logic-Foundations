package exercicios;
import java.util.Scanner;
public class Ex2_enquanto_faca {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		//Declaração de variáveis
		int n, fat;
		
		System.out.println("Digite um número: ");
		n = teclado.nextInt();
		
		fat = 1;
		
		while(n > 1) {
			fat *= n;
			n--;
		}
		System.out.println("Fatorial = " + fat);

	}

}
