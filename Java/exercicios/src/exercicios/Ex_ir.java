package exercicios;
import java.util.Scanner;
public class Ex_ir {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		double sal,ir,sal_liq;
		
		// Escreva "Digite Salário:"
		System.out.print("Digite salário: ");
		sal = entrada.nextDouble();
		if(sal <= 1900)
		{
			ir = 0;
		}
		else if (sal <= 2800)
			{
				ir = sal * 0.15;
			}
			else
			{
				ir = sal * 0.275;
			}
		
		sal_liq = sal - ir;
			
			System.out.println("IR: " + ir);
			System.out.println("Salário Líquido: " + sal_liq);
			
	}
}
