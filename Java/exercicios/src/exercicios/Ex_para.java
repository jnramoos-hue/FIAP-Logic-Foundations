package exercicios;
import java.util.Scanner;
public class Ex_para {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
				// Estancia o objeto Teclado para poder ler variáveis
				Scanner teclado = new Scanner(System.in);

				// Declaração das variáveis
				float i, n, soma = 0;
				System.out.println("Digite 10 números: ");

				for (i = 1; i <= 10; i++) {
					n = teclado.nextFloat();
					soma += n;
				}

				System.out.println("Somatória = " + soma);
			}
		
	}


