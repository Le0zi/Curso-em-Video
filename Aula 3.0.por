programa
{
	
	funcao inicio()
{
//Variaveis
cadeia nome
inteiro idade
real nota1, nota2, nota3, media

//Leitura de dados

escreva("Olá, informe seu nome completo: ")
leia(nome)
escreva("\ninforme sua idade: ")
leia(idade)
escreva("\nInforme as notas do primeiro, segundo e terceiro bimestre, na respectiva ordem : ")
leia(nota1, nota2, nota3)


//Informando resultado e calculando

media = (nota1 + nota2 + nota3) / 3

se (media >= 7){
	escreva(nome + " sua idade é " + idade + ", parabéns você foi aprovado, sua media é " + media)
	se (media == 10){
		escreva("\nVocê foi aprovado com nota maxima, parabéns")}
	
}
senao{
	escreva(nome + "sua idade é " + idade + ", você foi reprovado e sua media é "+ media)	
	}


escreva("\n***** FIM ****")

}

	
}


/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 747; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */