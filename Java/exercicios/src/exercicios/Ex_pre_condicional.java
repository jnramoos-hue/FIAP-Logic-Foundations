package exercicios;
import java.util.Scanner;
public class Ex_pre_condicional {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		String opcao;
		
		System.out.print("Digite [S]im ou [N]ão: ");
		opcao = entrada.next();
		
		while(!(opcao.equals("s") || opcao.equals("S") || opcao.equals("n") || opcao.equals("N")))
		{	
			System.out.println("Você digitou " + opcao + " digite S ou N! ");
			
			System.out.print("Digite [S]im ou [N]ão ");
			opcao = entrada.next();
		}
		
		System.out.println("Você digitou: " + opcao);
	}

}
