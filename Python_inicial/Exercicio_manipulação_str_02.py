import os
os.system("cls||clear")

"""Faça um programa que leia um numero de 0 a 9999 e mostre 
na tela cada um dos digitos separados"""

num=int(input("Informe um numero: "))

unidade = num//1 % 10
dezena = num//10 % 10
centena = num//100 % 10
milhar = num//1000 % 10

print(f"Milhar: {milhar}, Centena: {centena}, Dezena: {dezena}, Unidade: {unidade}")