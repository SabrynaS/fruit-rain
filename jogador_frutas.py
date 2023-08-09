import pygame,os
from random import randrange

largura = 600
altura = 500

tela = pygame.display.set_mode((largura, altura))

diretorio_principal = os.path.dirname(__file__)
diretorio_imagem = os.path.join(diretorio_principal, 'imagem')

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagem, 'girl.png')).convert_alpha()


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.andando_direita = []
        self.andando_esquerda = []

        for i in range(3):
            img = sprite_sheet.subsurface((i * 200, 0), (200, 200))
            self.andando_direita.append(img)

            img = sprite_sheet.subsurface((i * 200, 200), (200, 200))
            self.andando_esquerda.append(img)

        self.atual = 0
        self.image = self.andando_direita[self.atual]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 350)

        self.animar = False
        self.direcao = False

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= 3:
                self.atual = 0
                self.animar = False
            if self.direcao == True:
                self.image = self.andando_direita[int(self.atual)]
            else:
                self.image = self.andando_esquerda[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (150, 150))

    def moveRight(self, pixels):
        self.direcao = True
        self.rect.x += pixels
        self.animar = True
        if self.rect.x > 500:
            self.rect.x = 500

    def moveLeft(self, pixels):
        self.direcao = False
        self.rect.x -= pixels
        self.animar = True
        if self.rect.x < 0:
            self.rect.x = -40


class Fruta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frutinha = []
        self.frutinha.append(pygame.image.load('imagem/maca.png'))
        self.atual = 0
        self.image = self.frutinha[self.atual]
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = randrange(1, 500, 5)
        self.rect.x = randrange(1, 500, 5)

    def update(self):
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randrange(5, 500, 5)
        self.rect.y +=2

class Banana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bananinha = []
        self.bananinha.append(pygame.image.load('imagem/bananas.png'))
        self.atual = 0
        self.image = self.bananinha[self.atual]
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = randrange(1, 500, 5)
        self.rect.x = randrange(1, 500, 5)

    def update(self):
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randrange(5, 500, 5)
        self.rect.y += 2

class PeraMaca(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.peramaca = []
        self.peramaca.append(pygame.image.load('imagem/peramaca.png'))
        self.atual = 0
        self.image = self.peramaca[self.atual]
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = randrange(1, 500, 5)
        self.rect.x = randrange(1, 500, 5)

    def update(self):
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randrange(5, 500, 5)
        self.rect.y += 2

class FrutaPodre(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frutinhapodre = []
        self.frutinhapodre.append(pygame.image.load('imagem/macapodre.png'))
        self.atual = 0
        self.image = self.frutinhapodre[self.atual]
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = randrange(1, 500, 5)
        self.rect.x = randrange(1, 500, 5)

    def update(self):
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randrange(5, 500, 5)
        self.rect.y += 2
