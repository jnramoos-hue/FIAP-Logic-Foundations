package exercicios;
import java.util.Scanner;
public class Ex_op_var {
	public static void main (String[] args){
		
		Scanner entrada = new Scanner(System.in);
		
		int num,dobro;
		
		//Ler o numero
		System.out.print("Digite um numero: ");
		num = entrada.nextInt();
		
		//Calcular o cubo
		dobro = num * num * num;
		
		//Exibir o valor do cubo
		System.out.print("Resultado: " + dobro);
	
	}
}
