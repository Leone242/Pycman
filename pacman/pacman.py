import pygame
from abc import ABCMeta, abstractmethod
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont('arial', 24, True, False)

amarelo = (255, 255, 0)
azul = (0, 0, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

acima = 1
abaixo = 2
direita = 3
esquerda = 4

velocidade = 1

class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass


class Cenario(ElementoJogo):
    def __init__(self, tamanho, pac, fan):
        self.tamanho = tamanho
        self.pacman = pac
        self.fantasma = fan
        self.pontos = 0
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def exibe_pontos(self, tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render(f'Score: {self.pontos}', True, amarelo)
        tela.blit(img_pontos, (pontos_x, 50))

    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = preto
            if coluna == 2:
                cor = azul
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                cor = amarelo
            pygame.draw.circle(tela, cor, (x + half, y + half), self.tamanho // 10, 0)

    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.exibe_pontos(tela)

    def get_direcoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha -1)][int(coluna)] != 2:
            direcoes.append(acima)
        if self.matriz[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(abaixo)
        if self.matriz[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(esquerda)
        if self.matriz[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(direita)
        return direcoes

    def calcular_regras(self):
        direcoes = self.get_direcoes(self.fantasma.linha, self.fantasma.coluna)
        if len(direcoes) >= 3:
            self.fantasma.esquina(direcoes)

        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao
        if 0 <= col < 28 and 0 <= lin < 29:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[lin][col] == 1:
                    self.pontos +=1
                    self.matriz[lin][col] = 0

        col = int(self.fantasma.coluna_intencao)
        lin = int(self.fantasma.linha_intencao)
        if 0 <= col < 28 and 0 <= lin < 29 and self.matriz[lin][col] != 2:
            self.fantasma.aceitar_movimento()
        else:
            self.fantasma.recusar_movimento(direcoes)


    def processar_eventos(self, evts):
        for e in evts:
            if e.type == pygame.QUIT:
                exit()


class Pacman(ElementoJogo):
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.vel_x = 0
        self.vel_y = 0
        self.raio = self.tamanho / 2
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = (self.coluna * self.tamanho + self.raio)
        self.centro_y = (self.linha * self.tamanho + self.raio)

    def pintar(self, tela):
        pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, preto, pontos, 0)

        olho_x = int(self.centro_x + self.raio / 4)
        olho_y = int(self.centro_y - self.raio * 0.6)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = velocidade
                elif e.key == pygame.K_LEFT:
                    self.vel_x = - velocidade
                elif e.key == pygame.K_UP:
                    self.vel_y = - velocidade
                elif e.key == pygame.K_DOWN:
                    self.vel_y = velocidade
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def aceitar_movimento(self):
        self.coluna = self.coluna_intencao
        self.linha = self.linha_intencao

class Fantasma(ElementoJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 6
        self.linha = 8
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = 0
        self.tamanho = tamanho
        self.cor = cor


    def calcular_regras(self):
        if self.direcao == acima:
            self.linha_intencao -= self.velocidade
        elif self.direcao == abaixo:
            self.linha_intencao += self.velocidade
        elif self.direcao == direita:
            self.coluna_intencao += self.velocidade
        elif self.direcao == esquerda:
            self.coluna_intencao -= self.velocidade

    def mudar_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)

    def esquina(self, direcoes):
        self.mudar_direcao(direcoes)

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao


    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes)

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [
            (px, py + self.tamanho),
            (px + fatia*2, py + fatia*2),
            (px + fatia*3, py + fatia//2),
            (px +fatia*4, py),
            (px + fatia*6, py),
            (px +fatia*7, py + fatia//2),
            (px +fatia*7.75, py + fatia*2),
            (px +self.tamanho, py + self.tamanho)
        ]
        pygame.draw.polygon(tela, self.cor, contorno, 0)
        olho_raio_ext = fatia
        olho_raio_int = fatia // 2

        olho_e_x = int(px + fatia * 3)
        olho_e_y = int(py + fatia * 2.5)

        olho_d_x = int(px + fatia * 6)
        olho_d_y = int(py + fatia * 2.5)
        pygame.draw.circle(tela, branco, (olho_e_x, olho_e_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, preto, (olho_e_x, olho_e_y), olho_raio_int, 0)

        pygame.draw.circle(tela, branco, (olho_d_x, olho_d_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, preto, (olho_d_x, olho_d_y), olho_raio_int, 0)

    def processar_eventos(self, evts):
        pass


if __name__== '__main__':
    size = (600 // 30)
    pacman = Pacman(size)
    blinky = Fantasma(vermelho, size)
    cenario = Cenario(size, pacman, blinky)

    while True:
        pacman.calcular_regras()
        blinky.calcular_regras()
        cenario.calcular_regras()

        screen.fill(preto)
        cenario.pintar(screen)
        pacman.pintar(screen)
        blinky.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        eventos = pygame.event.get()

        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)
