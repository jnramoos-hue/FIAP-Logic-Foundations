package exercicios;
import java.util.Scanner;
public class Escolha_dia_semana {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		int dia;
		System.out.print("Digite um número: ");
		dia =  entrada.nextInt();
		
		switch(dia)
		{
		case 1: System.out.print("Domingo"); break;
		case 2: System.out.print("Segunda - feira"); break;
		case 3: System.out.print("Terça - feira"); break;
		case 4: System.out.print("Quarta - feira"); break;
		case 5: System.out.print("Quinta - feira"); break;
		case 6: System.out.print("Sexta - feira"); break;
		case 7: System.out.print("Sábado"); break;
		default: System.out.print("Dia inválido"); break;
		}
	}

}
