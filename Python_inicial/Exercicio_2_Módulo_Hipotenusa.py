import os 
os.system("cls||clear")
import math
#from math import hypot, para calculo de hipotenusa

"""Faça um programa que leia o comprimento do cateto oposto e do cateto 
adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa"""

#Entrada:

co=float(input("comprimento do cateto oposto: "))
ca=float(input("Comprimento do cateto adjancete: "))
hi= math.hypot(co,ca)

#Resultado:

print(f"Sua Hipotenusa é {hi:.2f}")