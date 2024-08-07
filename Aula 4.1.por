programa
{ 
	
	funcao inicio()
	{
//Variaveis

real numero1, numero2

//Declaração

escreva("Informe o primeiro numero: ")
leia(numero1)
escreva("\nInforme o segundo numero: ")
leia(numero2)

//resultado
se(numero1>numero2 e numero2<numero1){
	escreva(numero1 + " é maior que "+ numero2)
	escreva("\nO numero " + numero1 + " é maior")
	escreva("\nO numero " + numero2 + " é o menor")
	}
se(numero1<numero2 e numero2>numero1){
	escreva(numero2 + " é maior que " + numero1)
	escreva("\nO numero " + numero2 + " é maior")
	escreva("\nO numero " + numero1 + " é menor")

}
senao{
	escreva("\nAmbos os numeros são iguais" + numero1 + " , " + numero2)
}

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 600; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */