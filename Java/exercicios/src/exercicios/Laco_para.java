package exercicios;
import java.util.Scanner;
public class Laco_para {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		int num, cont, maior;
		
		System.out.println("Diget 5 numeros: ");
		num = entrada.nextInt();
		maior = num;
		
		for(cont = 1; cont <= 4; cont++)
		{
			num = entrada.nextInt();
			
			if(num > maior) {
				maior = num;
			}
		}
		System.out.println("Maior valor = " + maior);
		

	}

}
