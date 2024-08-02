programa
{
	
	funcao inicio(){
//Variaveis

cadeia nome
inteiro idade
real nota1, nota2, media

//Solicitação de dados

escreva("\nPor favor informe seu nome: ")
leia(nome)
escreva("\nPor favor informe sua idade: ")
leia(idade)
escreva("\nPor favor informe a primeira nota: ")
leia(nota1)
escreva("\nPor favor informe a primeira nota: ")
leia(nota2)

//Resultados

media = (nota1 + nota2) / 2
escreva("\nSua media é: " + media)
escreva("\n" + nome + "Sua media é " + media + ", e sua idade é " + idade)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 99; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */