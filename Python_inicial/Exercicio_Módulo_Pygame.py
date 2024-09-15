import os
os.system("cls||clear")
import pygame #Biblioteca para games
"""Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3"""
#Iniciando Biblioteca python para games

pygame.init()

#Procurando a musica:
pygame.mixer.music.load("Nome da musica.formato do arquivo")
#Dando play na musica:
pygame.mixer.music.play()
#Informando quando termiinar:
pygame.event.wait()

