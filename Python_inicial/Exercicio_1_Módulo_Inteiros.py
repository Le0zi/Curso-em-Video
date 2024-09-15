"""Crie um programa que leia um numero real de entrada pelo 
teclado e mostre sua parte inteira."""

from math import trunc #Retirando apenas numeros inteiro.
import os

os.system("cls||clear")

#Entrada de dados:

num=float(input("Informe um numero: "))

#Imprimindo resultado

print(f"Seu numero é {num} e sua parte inteira é {trunc(num)}")


#Resolvendo sem utilizar Math

num1=float(input("Informe um segundo numero: "))

print(f"Seu numero é {num1} e sua parte inteira é {int(num1)}")
