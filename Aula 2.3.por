programa
{
	
	funcao inicio(){

//Variaveis.

inteiro numero1, antecessor, sucessor

//Declaração de variaveis

escreva("Infomre o numero: ")
leia(numero1)

//calculo e resultado

antecessor = numero1 - 1
sucessor = numero1 + 1

escreva("\nO numero informado é " + numero1 + " , seu sucessor é " + sucessor + " 6e seu antecessor é " + antecessor)

se (antecessor>sucessor)
		escreva("\nAntecessor é maior que sucessor")
se (sucessor>antecessor)
		escreva("\nSucessor é maior que antecessor")

	}
	
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 497; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */