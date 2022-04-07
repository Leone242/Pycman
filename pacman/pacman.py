import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), 0)

amarelo = (255, 255, 0)
preto = (0, 0, 0)

velocidade = 1

class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800 // 30
        self.vel_x = 0
        self.vel_y = 0
        self.raio = self.tamanho / 2

    def calcula_regras(self):
        self.coluna += self.vel_x
        self.linha += self.vel_y
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

    '''def processar_eventos_mouse(self, eventos):
        delay = 60
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna =(mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay'''


if __name__== '__main__':
    pacman = Pacman()

    while True:
        pacman.calcula_regras()

        screen.fill(preto)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(60)

        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)
