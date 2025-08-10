import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# carregar músicas
pygame.mixer.music.load('../Projetos/audios/Snake Game - Theme Song.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('../Projetos/audios/smw_coin.wav')
barulho_colisao.set_volume(0.3)
som = pygame.mixer.Sound('../Projetos/audios/smw_dragon_coin.wav')
som.set_volume(0.1)

game_over = pygame.mixer.Sound('../Projetos/audios/smb_gameover.wav')
game_over.set_volume(0.06)

# criar tela e posições

largura = 940
altura = 680

x_cobra = largura / 2
y_cobra = (altura / 2) - 50

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(60, 680)
y_maca = randint(50, altura - 250)

x_pedra = randint(60, 680)
y_pedra = randint(50, altura - 250)

x_pedra2 = randint(60, 680)
y_pedra2 = randint(50, altura - 250)

x_poder = randint(60, 680)
y_poder = randint(50, altura - 250)

total = 0

# definir fontes das mensagens

fonte = pygame.font.SysFont('arial', 40, True, True)
fonte2 = pygame.font.SysFont('arial', 20, True, True)
fonte3 = pygame.font.SysFont('arial', 40, True, True)
fonte4 = pygame.font.SysFont('arial', 70, True, True)

# cores

amarelo = (255, 255, 0)
laranja = (255, 165, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
verde_escuro = (10, 110, 30)
cinza = (105, 105, 105)
azul_clarinho = (105, 89, 205)
azul_ceu = (135, 206, 250)
turquesa = (64, 224, 208)
verde_limao = (50, 205, 50)
roxo_lindao = (138, 43, 226)
violeta = (148, 0, 211)
roxo = (128, 0, 128)
preto = (0, 0, 0)
branco = (255, 255, 255)

# tela gerada
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 5

morreu = False

pontos = 0

# tabela_fundo = pygame.image.load('Capturar-removebg-preview (2).png').convert()
# tabela_fundo = pygame.transform.scale(tabela_fundo, (340, 100))

imagem_fundo = pygame.image.load('../Projetos/sprites/sprites1/img_1.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

imagem_menu = pygame.image.load('sprites/menu.png').convert()
imagem_menu = pygame.transform.scale(imagem_menu, (largura, altura))


def aumenta_cobra(lista_cobra, tela):
    """
    função faz com que aumente o tamanho da cobra
    :param lista_cobra: recebe a lista com as posições da cabeça da cobra
    :return: retorna mais pedaços da cobra
    """
    for XeY in lista_cobra:
        pygame.draw.rect(tela, amarelo, (XeY[0], XeY[1], 32, 32))


def reiniciar_jogo():
    """
    zera todos os pontos e redefine as posições
    :return: todos os valores zerados
    """
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu, velocidade, total, x_pedra, y_pedra, x_pedra2, y_pedra2
    pygame.mixer.music.play(-1)
    velocidade = 10
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura // 2
    y_cobra = (altura / 2) - 50
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(60, 880)
    y_maca = randint(50, altura - 250)
    morreu = False
    total = 0
    x_pedra = randint(60, 680)
    y_pedra = randint(50, altura - 250)
    x_pedra2 = randint(60, 680)
    y_pedra2 = randint(50, altura - 250)


class Maca(pygame.sprite.Sprite):
    """
    faz com que uma maçã seja gerada na tela
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('../Projetos/sprites/sprites1/sprite_20.png'))
        self.sprites.append(pygame.image.load('../Projetos/sprites/sprites1/sprite_21.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))

        self.rect = self.image.get_rect()
        self.rect.topleft = x_maca, y_maca

    def update(self):
        self.atual += 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))


class Pedra(pygame.sprite.Sprite):
    """
    faz com que uma pedra seja gerada na tela
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('../Projetos/sprites/sprites1/pedra0(1).png'))
        self.sprites.append(pygame.image.load('../Projetos/sprites/sprites1/pedra1(1).png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.atual += 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))


comecar = False

while True:
    # começo do loop para começar o jogo
    relogio.tick(30)
    tela.blit(imagem_fundo, (0, 0))

    mensagem4 = f'Velocidade: {velocidade}'
    texto_formatado4 = fonte.render(mensagem4, False, branco)

    mensagem3 = f'Total: {total}'
    texto_formatado3 = fonte.render(mensagem3, False, branco)

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, branco)

    menu = 'Aperte [Espaço] para iniciar.'
    texto_menu = fonte.render(menu, False, verde_escuro)

    if not comecar:
        tela.blit(imagem_menu, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    comecar = True
        tela.blit(texto_menu, (largura / 2 - 400, altura / 2 - 70))
        pygame.display.update()

    else:
        for event in pygame.event.get():
            # vai detectar se pressionou teclas específicas do teclado
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_RIGHT or event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_UP or event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade
                        x_controle = 0
                if event.key == K_DOWN or event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade
                        x_controle = 0

    if comecar:
        # faz com que a posição da cobra seja igual a direção com que o jogador queira
        x_cobra += x_controle
        y_cobra += y_controle

        # desenha tudo o que vai existir na tela, seja sprites, ou desenhos
        cobra = pygame.draw.rect(tela, amarelo, (x_cobra, y_cobra, 20, 20))
        sprites = pygame.sprite.Group()
        maca = Maca()
        pedra = Pedra(x_pedra, y_pedra)
        sprites.add(pedra)
        sprites.add(maca)
        pedra2 = Pedra(x_pedra2, y_pedra2)
        sprites.add(pedra2)
        sprites.draw(tela)
        linha1 = pygame.draw.line(tela, (125, 200, 65), (largura - 1, 0), (largura - 1, altura - 178), 5)
        linha2 = pygame.draw.line(tela, (125, 200, 65), (0, 0), (largura - 1, 0), 5)
        linha3 = pygame.draw.line(tela, (125, 200, 65), (0, 0), (0, altura - 178), 5)
        linha4 = pygame.draw.line(tela, (125, 200, 65), (0, altura - 178), (largura - 1, altura - 178), 5)

        """if maca.rect.topleft == pedra.rect.topleft:
            x_maca = randint(60, 680)
            y_maca = randint(50, altura - 250)"""

        if maca.rect.colliderect(pedra):
            x_maca = randint(60, 880)
            y_maca = randint(50, altura - 250)

        if cobra.colliderect(maca):
            x_maca = randint(60, 880)
            y_maca = randint(50, altura - 250)

            pontos += 1
            barulho_colisao.play()
            total += 10
            if pontos % 10 == 0:
                som.play()
                barulho_colisao.stop()
                velocidade += 1
                total += 20
            comprimento_inicial += 1

        """if cobra.colliderect(poder):
            x_poder = randint(60, 880)
            y_poder = randint(50, altura - 250)
            if cobra.colliderect(maca):
                pontos += 2
            if pontos % 15 == 0:
                break"""

        lista_cabeca = [x_cobra, y_cobra]

        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0]

        lista_cobra.append(lista_cabeca)

        """tempo += 0.03
        tempo_texto = fonte.render('Tempo: ' + str(tempo), True, branco, preto)"""

        if lista_cobra.count(lista_cabeca) > 1 or cobra.colliderect(linha1) \
                or cobra.colliderect(linha2) or cobra.colliderect(linha3) or cobra.colliderect(linha4) or cobra.colliderect(pedra):
            game_over_texto = 'Game'
            game_over_texto2 = 'Over'
            game_formatado2 = fonte4.render(game_over_texto2, False, branco)
            game_formatado = fonte4.render(game_over_texto, False, branco)
            mensagem2 = 'Pressione a tecla R para jogar novamente.'
            texto_formatado2 = fonte2.render(mensagem2, True, branco)
            ret_texto = texto_formatado2.get_rect()
            ret_texto2 = game_formatado.get_rect()
            ret_texto3 = game_formatado2.get_rect()
            game_over.play()
            morreu = True
            while morreu:
                pygame.mixer.music.stop()
                tela.fill(preto)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()
                            game_over.stop()

                ret_texto.center = (largura // 2, altura // 2 + 61)
                ret_texto2.center = (largura // 2, 250)
                ret_texto3.center = (largura // 2, 320)
                tela.blit(texto_formatado2, ret_texto)
                tela.blit(game_formatado, ret_texto2)
                tela.blit(game_formatado2, ret_texto3)
                pygame.display.update()

        aumenta_cobra(lista_cobra, tela)

        """tela.blit(tempo_texto, (400, 400))"""
        tela.blit(texto_formatado, (630, 580))
        tela.blit(texto_formatado3, (80, 580))
        tela.blit(texto_formatado4, (300, 580))
        pygame.display.update()
