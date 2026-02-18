package exercicios;
import java.util.Scanner;
public class Ex_pos_condicional {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Estancia o objeto Teclado para ler variáveis
		Scanner teclado = new Scanner(System.in); 
		
		// Declaracao de variáveis
		int hug, zez, lui, voto;
		
		// zera as variáveis dos candidatos
		hug = zez = lui = 0;
		System.out.println("1 - Huguinho: ");
		System.out.println("2 - Zezinho: ");
		System.out.println("3 - Luizinho: ");
		System.out.println("0 - SAIR: ");
		
		// Inicio do laca Faca-enquanto
		do {
			System.out.println("Digite o voto: ");
			voto = teclado.nextInt();
			switch(voto) {
				case 1 : hug++; break;
				case 2 : zez++; break;
				case 3 : lui++; break;
				default : System.out.println("Voto inválido, digite: 1, 2 ou 3");
			}
		}while(voto != 0);
		
		// Exibe o resultado da apuracao
		System.out.println("1 - Huguinho: " + hug + "votos");
		System.out.println("2 - Zezinho: " + zez + "votos");
		System.out.println("3 - Luizinho: " + lui + "votos");

	}

}
