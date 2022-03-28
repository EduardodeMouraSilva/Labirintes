import pygame as pg

pg.init()
# Janela
ALTURA = 16 * 30
LARGURA = 16 * 40

A = ALTURA
L = LARGURA

# Cores
BRANCO = (255, 255, 255)
AMARELO = (200, 200, 0)
AZUL_AGUA = (0, 100, 100)
AZUL = (0, 100, 200)

# Imagens
imagem_fundo = pg.image.load('imagem/plains.png')

# Sons
abertura = pg.mixer.Sound('musicas/little town - orchestral.ogg')
andar = pg.mixer.Sound('musicas/SnowWalk2.ogg')
andar.set_volume(0.05)
