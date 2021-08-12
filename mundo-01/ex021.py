"""EXERCÍCIO 021 - TOCANDO UM MP3
Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3.
"""

import pygame
import time

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('D:/projetos/aprendendo-python/mundo-01/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
parar = input('Digite algo para parar!!!')
#time.sleep(360)