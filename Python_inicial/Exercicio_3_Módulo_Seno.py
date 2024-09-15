import os
os.system("cls||clear")
from math import sin, cos, tan, radians #Especificando quais operações eu vou utilizar no codigo.

"""Faça um programa que leia um ângulo 
qualquer e mostre na tela o valor do seno, cosseno e 
tangente desse ângulo."""

#Entrada:

ang=float(input("Informe o ângulo: "))

#Calculando:

sen=sin(radians(ang))
cose=cos(radians(ang))
tang=tan(radians(ang))

#Resultado:
print(f"O seno de {ang}° é {sen:.2f}\nO cosseno de {ang}° é {cose:.2f}\nA tangente de {ang}° é {tang:.2f}")