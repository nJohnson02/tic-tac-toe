import pygame
import time

class Game:
    def __init__(self):
        self.board = [['x', 'o', 'o'],['-', '-', '-'],['x', 'x', 'o']]

    def checkForWin(self):
        pass
    
    def draw(self):
        #Setup pygame window
        pygame.init()
        print(pygame.font.get_fonts())
        clock = pygame.time.Clock()
        pygame.display.set_caption('Tic Tac Toe!')
        window = pygame.display.set_mode((800,800))

        #Define constants for colors and fonts
        BACKGROUND_COLOR = '#222222'
        FOREGROUND_COLOR = '#1180E5'
        FONT = pygame.font.SysFont('arialBlack', 300)
        
        #yes
        window.fill(BACKGROUND_COLOR)

        #draw the grid
        pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(265, 50, 5, 700))
        pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(532, 50, 5, 700))
        pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(50, 265, 700, 5))
        pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(50, 532, 700, 5))

        img = FONT.render('o', True, FOREGROUND_COLOR)
        window.blit(img, (50, -100))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.update()
            clock.tick(60) 