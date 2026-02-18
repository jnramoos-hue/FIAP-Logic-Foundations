package exercicios;
import java.util.Scanner;
public class Ex_modulo_num {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		int n;
		System.out.println("Digite um número: ");
		n = entrada.nextInt();
		// Decisão simples: Verifica se o número é negativo
		if(n < 0)
		{ // Se verdade executa este bloco
			
			n = n * -1;
		}
		//Exibe um número positivo
		System.out.println("Módulo: " + n);
	}

}
