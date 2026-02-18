package exercicios;
import java.util.Scanner;
public class Pos_condicional {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		int num,soma = 0;
		
		do {
			System.out.println ("Digite um numero : ");
			num = entrada.nextInt();
			if(num > 0)
			{	
				soma = soma + num;
			}
		}while(num >= 0 );
		System.out.print("Soma = " + soma);
	}

}
