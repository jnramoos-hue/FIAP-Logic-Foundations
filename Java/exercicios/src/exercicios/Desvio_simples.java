package exercicios;
import java.util.Scanner;
public class Desvio_simples {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		double venda, desconto;
		
		//Escreva “Digite o valor da venda: ”
		System.out.print("Digite o valor da venda: ");
		//Leia venda
		venda = entrada.nextDouble();
		
		//se venda  >  300 então
		if ( venda > 300)
		{
			//desconto = venda * 10 / 100
			desconto = venda * 10 / 100 ;
			
			//venda = venda - desconto
			venda = venda - desconto;	
			
		//fim_se
		}
		
		System.out.print("Novo valor = " + venda);
		//Escreva “Novo valor =  ” , venda
	}

}
