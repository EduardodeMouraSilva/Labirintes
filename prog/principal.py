import os
from sys import exit
 
import pygame as pg

from classes import Quadrado, Seguir
from variavel import *



pg.init()

### Configurações da janela
janela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption('Labirintes')

### Instâncias da classe quadrado
Grupo = pg.sprite.Group()
Mouse = Seguir()
tam = (500, 70)
cores = (AZUL_AGUA, AMARELO, AZUL)
Quad = Quadrado((70, 1.5), 'Jogar', tam, Mouse, cores)
Quad2 = Quadrado((70, 2.5), 'Como Jogar', tam, Mouse, cores)
Quad3 = Quadrado((70, 3.5), 'Créditos', tam, Mouse, cores)

Grupo.add(Quad, Quad2, Quad3, Mouse)

## Texto
times_new = pg.font.SysFont('Times new Roma', 80)
nome_jogo = times_new.render('Labirintes', False, AMARELO)

relogio = pg.time.Clock()

Continuar = True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    janela.blit(imagem_fundo, (0, 0))
    janela.blit(nome_jogo, ((L - nome_jogo.get_width())/2, A/5 * 0.4))

    Grupo.draw(janela)
    Grupo.update()

    if pg.mouse.get_pressed() == (1, 0, 0):
        if pg.sprite.collide_rect(Mouse, Quad):
            continuar = False
            pg.quit()
            os.startfile('prog\janela.py', operation='open')
            exit()
        elif pg.sprite.collide_rect(Mouse, Quad2):
            continuar = False
            pg.quit()
            os.startfile('prog\como_jogar.py')
            exit()
        elif pg.sprite.collide_rect(Mouse, Quad3):
            continuar = False
            pg.quit()
            os.startfile('prog\creditos.py')
            exit()
    
    pg.display.update()
