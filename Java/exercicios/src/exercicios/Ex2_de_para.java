package exercicios;
import java.util.Scanner;
public class Ex2_de_para {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		//Declaração de variáveis 
		float preco_maco, qtd_maco, anos, dias_fumante, custo;
		// Solicitar os dados ao usuário
		System.out.println("Digite o preço do maço: ");
		preco_maco = entrada.nextFloat();
		System.out.println("Digite a quantidade de maços: ");
		qtd_maco = entrada.nextFloat();
		System.out.println("Digite a quantidade de anos que fuma: ");
		anos = entrada.nextFloat();
	
		// Calcula a qtd. de dias como fumante
		dias_fumante = anos * 365;
		// Calcula a qtd. de dias como fumante
		dias_fumante = anos * 365;
		// Calcula o gasto do tempo que fuma
		custo = dias_fumante * preco_maco;
		// Exibe o custo
		System.out.println("Voce já gastou £" + custo + " Fumando");

	}

}
