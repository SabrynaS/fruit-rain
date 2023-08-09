import pygame, sys,os, jogador_frutas
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

'''pygame.mixer.music.set_volume(0.07)
musicafundo = pygame.mixer.music.load('som/Girls.wav')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('som/colisao.wav')
gameoversom = pygame.mixer.Sound('som/gameover.wav')'''

largura = 600
altura = 500
pontos = 0
gameover1 = False
querojogar = False
venceu = False

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fruit Rain')
fonte = pygame.font.SysFont('times new roman', 30, True, False)


def menu():
    global querojogar,venceu
    tela.blit(imagem_menu, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.time.delay(200)
                querojogar = True
                venceu = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

def menu2():
    while querojogar==False:
        menu()

def reiniciar():
    global pontos, colisao1
    pontos = 0
    jogador.rect.topleft = (100, 350)
    jogador.atual = 0
    jogador.image = jogador.andando_direita[jogador.atual]
    jogador.animar = False
    maca.rect.y = 0
    maca.rect.x = randrange(1, 500, 5)
    peramaca.rect.y =  0
    peramaca.rect.x =  randrange(1, 500, 5)
    banana.rect.y = 0
    banana.rect.x = randrange(1, 500, 5)
    fruta_podre.rect.y = 0
    fruta_podre.rect.x = randrange(1, 500, 5)

def ganhou():
    global venceu

    flag = True

    while flag:
        tela.blit(imagem_vencedor, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    venceu = False
                    reiniciar()
                    while venceu == False:
                        menu()
                    flag = False

def game_over():
    mensagem = f'{pontos}'
    texto_pontos = fonte.render(mensagem, True, (0, 0, 0))
    rect_text2 = texto_pontos.get_rect()
    #gameoversom.play()
    gameover1= True

    while gameover1:
        tela.blit(imagem_gameover,(0,0))
        #tela.fill((0,0,0))
        rect_text2= (340, 110)
        tela.blit(texto_pontos, rect_text2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   reiniciar()
                   gameover1 = False

def nivel():

    if pontos>=50:
        texto_pontos = fonte.render(mensagem, True, (255, 255, 255))
        tela.blit(imagem_nivel, (0, 0))
        tela.blit(texto_pontos, (230, 20))
        desenha_tela()
        maca.rect.y += 2.01
        banana.rect.y += 2.01
        peramaca.rect.y+=2.01
        fruta_podre.rect.y += 3

    if 70<pontos < 90 :
        nivel2 = f'Quase lá !'
        texto_nivel = fonte.render(nivel2, True, (255, 255, 255))
        tela.blit(texto_nivel, (225, 100))
    if pontos >= 100:
        ganhou()

def desenha_tela():
    grupo_jogador.draw(tela)
    grupo_banana.draw(tela)
    grupo_maca.draw(tela)
    grupo_peramaca.draw(tela)
    grupo_jogador.update()
    grupo_maca.update()
    grupo_banana.update()
    grupo_peramaca.update()
    if pontos >= 20:
        grupo_fruta_podre.draw(tela)
        grupo_fruta_podre.update()


grupo_jogador = pygame.sprite.Group()
jogador = jogador_frutas.Jogador()
grupo_jogador.add(jogador)

grupo_maca = pygame.sprite.Group()
maca = jogador_frutas.Fruta()
grupo_maca.add(maca)

grupo_banana = pygame.sprite.Group()
banana = jogador_frutas.Banana()
grupo_banana.add(banana)

grupo_peramaca = pygame.sprite.Group()
peramaca = jogador_frutas.PeraMaca()
grupo_peramaca.add(peramaca)


grupo_fruta_podre = pygame.sprite.Group()
fruta_podre = jogador_frutas.FrutaPodre()
grupo_fruta_podre.add(fruta_podre)


imagem_menu = pygame.image.load('imagem/fundo_inicio.png').convert_alpha()
imagem_menu = pygame.transform.scale(imagem_menu, (largura, altura))
imagem_fundo = pygame.image.load('imagem/'
                                 'fundo.jpeg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
imagem_nivel = pygame.image.load('imagem/nivel.jpg')
imagem_nivel= pygame.transform.scale(imagem_nivel, (largura, altura))
imagem_gameover = pygame.image.load('imagem/g1.png').convert_alpha()
imagem_gameover = pygame.transform.scale(imagem_gameover, (largura, altura))
imagem_vencedor= pygame.image.load('imagem/fundoganhou.png')
imagem_vencedor = pygame.transform.scale(imagem_vencedor, (largura, altura))


relogio = pygame.time.Clock()

while True:
    menu2()
    relogio.tick(100)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos:{pontos}'
    texto_pontos = fonte.render(mensagem, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        jogador.moveRight(7)

    if keys[pygame.K_LEFT]:
        jogador.moveLeft(4)


    colisao_fruta_podre = pygame.sprite.spritecollide(jogador, grupo_fruta_podre, False, pygame.sprite.collide_mask)
    colisao_com_maca = pygame.sprite.spritecollide(jogador, grupo_maca, False, pygame.sprite.collide_mask)
    colisao_com_banana = pygame.sprite.spritecollide(jogador, grupo_banana, False, pygame.sprite.collide_mask)
    colisao_com_pera_maca = pygame.sprite.spritecollide(jogador, grupo_peramaca, False, pygame.sprite.collide_mask)


    if colisao_fruta_podre:
      game_over()


    if colisao_com_maca:
         maca.rect.y = 0
         maca.rect.x = randrange(1, 500, 5)
         pontos = pontos + 1
         #barulho_colisao.play()

    if colisao_com_banana:
         banana.rect.y =0
         banana.rect.x = randrange(1, 500, 5)
         pontos = pontos + 5
         #barulho_colisao.play()

    if colisao_com_pera_maca:
         peramaca.rect.y =0
         peramaca.rect.x = randrange(1, 500, 5)
         pontos = pontos + 10
         #barulho_colisao.play()

    tela.blit(imagem_fundo, (0, 0))
    tela.blit(texto_pontos, (230,20))
    desenha_tela()

    nivel()

    pygame.display.flip()
