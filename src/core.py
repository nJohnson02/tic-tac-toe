#Import dependencies
import os
import time
import matplotlib
import pygame

#Import the other project filess
import functions.game as gameModule
import functions.ai as aiModule

#a function to clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Game engine (main program)
#create a game object
game = gameModule.Game()
game.draw()

    #take in game parameters

    #start the game (while loop)
        #draw board
        #player1 makes move
        #check for win
        #draw board
        #player2 makes move
        #check for win

#mental illness

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

img = FONT.render('x', True, FOREGROUND_COLOR)
window.blit(img, (50, -100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            _ = pygame.mouse.get_pos()
            exit()
    pygame.display.update()
    clock.tick(60) 
