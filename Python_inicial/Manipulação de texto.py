import os
os.system("cls||clear")

frase : str


frase = "Leonardo Machado Britto Junior"


print(frase[0:9])


quantidade = len(frase) #Len= Comprimento da frase.
quantidade1=frase.count("o") #count= Contagem de quantas vezes alguma caracter aparece.
quantidade2 = frase.find("gli") #find = determina o inicio de alguma informação determinada .
#caso o find retorne -1 quer dizer que não existe.
verificação='pia' in frase #in = Verifica se existe determinado texto dentro da variavel, caso exista ela informa true, caso não ela informa false.
substituição=frase.replace("Leonardo","Corno") #Efetua substituição de um texto selecionado por um outro predefinido.
maiuscula=frase.upper() #Transforma toda a variavel em maiscula.
minuscula=frase.lower() #Transforma toda a variavel em minuscula.
inicial=frase.capitalize() #Deixa apenas o primeiro caracter como maiusculo.
inicial_pv=frase.title() #Transforma iniciais de todas as palavras em maiusculo.
remoção=frase.strip() #Removo espaços excedentes no inicio e no final do texto
#ao mudar para (lstrip) ele remove da direita, e (rstrip) remove da esquerda.
separação=frase.split() #Faz a separação da frase em pedaços gerando "listas" novas.
junção = '-'.join(separação)






print(quantidade)
print(quantidade1)
print(quantidade2)
print(verificação)
print(substituição)
print(maiuscula)
print(minuscula)
print(inicial)
print(inicial_pv)
print(remoção)
print(separação[0])
print(junção)

