"""Faça um programa que leia um numero inteiro, e informe
a tabuada."""

import os
os.system("cls||clear")

print("\n=== INICIO ===\n")
num = int(input("Informe o numero que deseja receber a tabuada: "))
print("\n=== Tabuada ===\n")
for i in range(10):
    print(f"{num} X {i} = {num*i}")
print("\n=== FIM ===")