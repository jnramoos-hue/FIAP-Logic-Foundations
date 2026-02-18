package exercicios;
import java.util.Scanner;
public class Ex_entrada_dados {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner (System.in);
		int num, dobro;
		
		System.out.print("Digite um numero: ");
		num = entrada.nextInt();
		dobro = num + num;
		System.out.print("Dobro = " + dobro);
		
	}

}
