from os import startfile
from sys import exit

import pygame as pg

from variavel import *



pg.init()

janela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption('Labirintes')

fonte = pg.font.SysFont('Times new Roma', 80)
como1 = fonte.render('Use as setas do', False, BRANCO)
como2 = fonte.render('teclado para jogar.', False, BRANCO)

continuar = True
while continuar:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            startfile('prog\principal.py')
            exit()
    
    janela.blit(como1, (0, 0))
    janela.blit(como2, (0, 100))
    pg.display.update()
