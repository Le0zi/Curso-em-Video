import os
os.system("cls||clear")

"""Crie um programa que leia o nome completo de uma pessoa e mostre:
1- o Nome com todas as letras maiusculas.
2- o Nome com todas as letras minusculas.
3- Quantas letras sem considerar espaços.
4- Quantas letras tem o primeiro nome. """


nome = str(input("Nome: "))


print(f"Nome: {nome.upper()}")
print(f"Nome: {nome.lower()}")
nome1=nome.split()
nome2=''.join(nome1)
print(f"Quantidade de letras: {len(nome2)}")
print(f"Quantidade de letras no primeiro nome: {len(nome1[1])}")
