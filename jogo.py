import pygame as pg 
import random
import sys

# 1- Inicialização do Pygame
# Configuração da Tela
pg.init()
#LARGURA = 600
#ALTURA = 400
LARGURA, ALTURA = 600, 400
tela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption("Apanhador de Estrelas")
relogio = pg.time.Clock()

# 2- Set de cores (RGB)
PRETO = (20, 20, 20)
AZUL = (50, 150, 255)
AMARELO = (255, 215, 0)
BRANCO = (255, 255, 255)

# 3- Configurações do jogador
jogador_largura = 60
jogador_altura = 40
jogador_x = LARGURA // 2 - jogador_largura // 2
jogador_y = ALTURA - 40
velocidade_jogador = 7

# 4- Configurações da estrela
estrela_tamanho = 20
estrela_x = random.randint(0, LARGURA - estrela_tamanho)
estrela_y = 0
velocidade_estrela = 4

# 5- Pontuação e Fonte
pontos = 0
fonte = pg.font.SysFont(None, 36)

# 6- Looping Principal do Jogo
rodando = True

while rodando:
    # a- Evento de fechar o jogo
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

    # b- Movimentação do personagem
    teclas = pg.key.get_pressed()

    if teclas[pg.K_LEFT] and jogador_x > 0:
        jogador_x -= velocidade_jogador
    if teclas[pg.K_RIGHT] and jogador_x < LARGURA - jogador_largura:
        jogador_x += velocidade_jogador

    # c- MOVIMENTAÇÃO DA ESTRELA
    estrela_y += velocidade_estrela

    # d- COLISÕES
    rect_jogador = pg.Rect(jogador_x, jogador_y, jogador_largura, jogador_altura)
    rect_estrela = pg.Rect(estrela_x, estrela_y, estrela_tamanho, estrela_tamanho)

    if rect_jogador.colliderect(rect_estrela):
        pontos += 1
        estrela_x = random.randint(0, LARGURA - estrela_tamanho)
        estrela_y = 0
        velocidade_estrela += 0.2

    if estrela_y > ALTURA:
        estrela_x = random.randint(0, LARGURA - estrela_tamanho)
        estrela_y = 0
    
    # e- DESENHAR A TELA
    tela.fill(PRETO)

    # f- DESENHAR JOGADOR E ESTRELA
    pg.draw.rect(tela, AZUL, rect_jogador)
    pg.draw.rect(tela, AMARELO, rect_estrela)

    # g- EXIBIR PONTUAÇÃO
    texto_pontos = fonte.render(f"PONTOS: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    # h- ATUALIZA A TELA
    pg.display.flip()
    relogio.tick(60)

pg.quit()
sys.exit()