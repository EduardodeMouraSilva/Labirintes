from os import startfile
from sys import exit

import pygame as pg

from variavel import *



pg.init()

janela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption('Labirintes')

relogio = pg.time.Clock()

fonte = pg.font.SysFont('Times new roma', 60)
criador = fonte.render('Eduardo de Moura Silva', False, BRANCO)
email = fonte.render('eduardobrmasd@gmail.com', False, BRANCO)

a = 0

continuar = True
while continuar:
    relogio.tick(20)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            startfile('prog\principal.py')
            exit()
    janela.fill((0, 0, 0))
    janela.blit(criador, (20, ALTURA - a))
    janela.blit(email, (20, ALTURA + 50 - a))
    a += 1
    if a > 600:
        a = 0
    pg.display.update()
