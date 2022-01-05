from os import startfile
from sys import exit

import pygame as pg

from classes import Quadrado, Seguir
from variavel import *



pg.init()

janela = pg.display.set_mode((LARGURA/2, ALTURA/2))
pg.display.set_caption('Labirintes')

#Instâncias
Sprite = pg.sprite.Group()
Mouse = Seguir()
cores = (AZUL_AGUA, AMARELO, AZUL)
JogarNov = Quadrado((35, 1), 'Jogar Novamente', (250, 35), Mouse, cores, 
    letra=30)
TelaIni = Quadrado((35, 1.5), 'Tela Inicial', (250, 35) , Mouse, cores,
letra=30) 
Sair = Quadrado((35, 2), 'Sair', (250, 35), Mouse, cores, letra=30)

Sprite.add(Mouse, JogarNov, TelaIni, Sair)

fonte = pg.font.SysFont('Times new roma', 40)
ganhou = fonte.render('Você ganhou!!!', False, AMARELO)

continuar = True
while continuar:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuar = False
            pg.quit()
            exit()
    
    janela.blit(imagem_fundo, (0, 0))
    janela.blit(ganhou, (((L/2) - ganhou.get_width())/ 2, (A/2) * 0.2))
    Sprite.draw(janela)
    Sprite.update()
    pg.display.update()

    if pg.mouse.get_pressed() == (1, 0, 0):
        if pg.sprite.collide_rect(Mouse, JogarNov):
            pg.quit()
            startfile('prog\janela.py')
            exit()
        elif pg.sprite.collide_rect(Mouse, TelaIni):
            pg.quit()
            startfile('prog\principal.py')
            exit()
        elif pg.sprite.collide_rect(Mouse, Sair):
            pg.quit()
            exit()
