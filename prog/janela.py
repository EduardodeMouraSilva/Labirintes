from os import startfile
from sys import exit

import pygame as pg

from labirintos import labirinto1
from variavel import *



pg.init()


## Classe do personagem
class Personagem(pg.sprite.Sprite):
    def __init__(self, imagem, blocos):
        pg.sprite.Sprite.__init__(self)
        self.im = imagem
        self.imag = list()
        for ci in range(2):
            for i in range(8):
                self.ima = pg.Surface.subsurface(self.im, ((16 * i, 16 * ci), (16, 16)))
                self.imag.append(self.ima)
        self.quad = 4
        self.image = self.imag[self.quad]

        self.rect = self.image.get_rect()
        self.rect.left = 16 * 1
        self.rect.top = 16 * 1

        self.blocos = blocos

        # Atributos do personagem
        self.velocidade = 4
        self.coli = False

    def update(self, tecla):
        colisao = pg.sprite.spritecollide(self, self.blocos, False)

        if colisao:
            for i in colisao:
                
                if  self.rect.left > i.rect.left and self.rect.right > i.rect.right:
                    self.rect.left = i.rect.right
                elif self.rect.right < i.rect.right and self.rect.left < i.rect.left:
                    self.rect.right = i.rect.left
                elif self.rect.bottom > i.rect.bottom and self.rect.top > i.rect.top:
                    self.rect.top = i.rect.bottom
                elif self.rect.top < i.rect.top and self.rect.bottom < i.rect.bottom:
                    self.rect.bottom = i.rect.top
        
    def mover(self, tecla):
        self.update(tecla)
        if tecla == pg.K_LEFT:
            self.rect.left -= self.velocidade
        elif tecla == pg.K_RIGHT:
            self.rect.left += self.velocidade
        elif tecla == pg.K_UP:
            self.rect.top -= self.velocidade
        elif tecla == pg.K_DOWN:
            self.rect.top += self.velocidade
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
    
    def animar(self, tecla):
        self.quad += 1
        if tecla == pg.K_LEFT:
            if self.quad < 8 or self.quad > 11:
                self.quad = 8
        elif tecla == pg.K_RIGHT:
            if self.quad < 12 or self.quad > 15:
                self.quad = 12
        elif tecla == pg.K_UP:
            if self.quad > 3:
                self.quad = 0
        elif tecla == pg.K_DOWN:
            if self.quad < 4 or self.quad > 7:
                self.quad = 4

        self.image = self.imag[self.quad]



## Classe das paredes
class Parede(pg.sprite.Sprite):
    def __init__(self, imagem, x, y):
        pg.sprite.Sprite.__init__(self)
        self.im = imagem
        self.image = pg.Surface.subsurface(self.im, ((0,0), (16, 16)))

        self.rect = self.image.get_rect()
        self.rect.left = 16 * x
        self.rect.top = 16 * y

    def update(self):
        pass



## Classe das moedas
class Moeda(pg.sprite.Sprite):
    def __init__(self, imagem):
        pg.sprite.Sprite.__init__(self)
        self.im = imagem
        self.imagens = list()
        for i in range(6):
            self.imag = pg.Surface.subsurface(self.im, (9 * i, 0), (9, 10))
            self.imagens.append(self.imag)
        
        self.quad = 0
        self.image = self.imagens[self.quad]

        self.rect = self.image.get_rect()
        self.rect.left = 19
        self.rect.top = 467
    
    def update(self):
        self.quad += 1
        if self.quad > 5:
            self.quad = 0
        self.image = self.imagens[self.quad]



## Instanciando as classes e colocando no grupo 
Sprites = pg.sprite.Group()
Parede_bloco = pg.sprite.Group()

i_parede = pg.image.load('imagem/scraps_bricks.png')
# Algoritmo para ler o arquivo das paredes
for y,a in enumerate(labirinto1):
    for x,b in enumerate(a):
        if b == '-':
            Para = Parede(i_parede, x, y)
            Sprites.add(Para)
            Parede_bloco.add(Para)

i_moeda = pg.image.load('imagem/spin_coin_big_strip6.png')
Moedas = Moeda(i_moeda)
Sprites.add(Moedas)

i_perso = pg.image.load('imagem/hero.png')
Perso = Personagem(i_perso, Parede_bloco)
Sprites.add(Perso)

## Configurando a janela
janela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption("Labirites")

relogio = pg.time.Clock()


## O laço de repetição
continuar = True
while continuar:
    relogio.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuar = False
            pg.quit()
            exit()
    if event.type == pg.KEYDOWN:
        tecla = event.key
        Perso.mover(tecla)
        Perso.animar(tecla)
    
    if pg.sprite.collide_rect(Moedas, Perso):
        continuar = False
        startfile('prog\ganhou.py')
            
    Moedas.update()
    janela.blit(imagem_fundo, (0,0))
    Sprites.draw(janela)
    pg.display.update()
    