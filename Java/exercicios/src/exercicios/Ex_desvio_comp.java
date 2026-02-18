package exercicios;
import java.util.Scanner;
public class Ex_desvio_comp {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner (System.in);
		int tc;
		double sal, aumento, novo_sal;
		
		// Escreva "Digite o seu tempo de casa: "
		System.out.print("Digite o seu tempo de casa: ");
		//Leia tc
		tc = entrada.nextInt();
		//Escreva "Digite seu salário: "
		System.out.print("Digite seu salário: ");
		//Leia sal
		sal = entrada.nextDouble();
		
		//Se tc < 3 entao
		if (tc < 3) {
			//aumento = salario * 0.05
			aumento = sal * 0.05;
		}
		else {
			//aumento = salario * 0.1
			aumento = sal * 0.1;
		}
		//novo_sal = sal + aumento
		novo_sal = sal + aumento;
		
		//Escreva "O seu salário foi de " + sal + "par " + novo_sal
		System.out.print("O seu salário foi de " + sal + "par " + novo_sal);
	}

}
