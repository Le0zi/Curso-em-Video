import random #Biblioteca Random gera um numero aleatorio
import time
import os

os.system("cls||clear")

for i in range(1000):
    num = random.randint(-100,1000) #Informando o limite maximo e minimo ao qual o numero deve pertencer
    #Ao utilizar o Random.Randon ele informa um numero real entre 0 e 1, ao utilizar Random.Randint ele informa numeros aleatorios.
    print(f"{num} x {i} = {num*i}")
    time.sleep(1)