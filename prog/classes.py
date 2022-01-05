from variavel import *


class Quadrado(pg.sprite.Sprite):
    def __init__(self, pos, nome, tam, coli, cores, letra=60):
        pg.sprite.Sprite.__init__(self)
        x, y = pos
        self.nome = nome
        self.largura, self.altura = tam
        self.coli = coli
        self.cor1, self.cor2, self.cor3 = cores
        self.letra = letra

        self.image = pg.Surface(tam)
        self.image.fill(self.cor1)

        self.rect = self.image.get_rect()
        self.rect.top = (A/5 * y)
        self.rect.left = x

        fonte = pg.font.SysFont('Times new Roma', self.letra)
        self.nome = fonte.render(self.nome, False, self.cor2)
        self.image.blit(self.nome, ((self.largura - self.nome.get_width())/2,
            (self.altura - self.nome.get_height())/2))
    
    def update(self):
        if pg.sprite.collide_rect(self, self.coli):
            self.image.fill(self.cor3)
            self.image.blit(self.nome, ((self.largura-self.nome.get_width())/2,
            (self.altura - self.nome.get_height())/2))
        else:
            self.image.fill(self.cor1)
            self.image.blit(self.nome, ((self.largura-self.nome.get_width())/2,
            (self.altura - self.nome.get_height())/2))



class Seguir(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((1, 1))

        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0

    def update(self):
        x, y = pg.mouse.get_pos()
        self.rect.top = y
        self.rect.left = x

