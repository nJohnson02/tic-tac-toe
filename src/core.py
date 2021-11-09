#Import dependencies
import random
import matplotlib
import pygame

def draw(letter, position):
    positions = [(50, -100), (300, -100), (550, -100), (50, 150), (300, 150), (550, 150), (50, 400), (300, 400), (550, 400)]
    shape = FONT.render(letter, True, FOREGROUND_COLOR)
    window.blit(shape, positions[position])
    

#Create a game board
board = [['x', 'o', 'o'],['-', '-', '-'],['x', 'x', 'o']] #This is just for testing

#Initialize pygame
pygame.init()

#Define constants for colors and fonts
BACKGROUND_COLOR = '#222222'
FOREGROUND_COLOR = '#1180E5'
FONT = pygame.font.SysFont('arialBlack', 300)

#Create window
clock = pygame.time.Clock()
pygame.display.set_caption('Tic Tac Toe!')
window = pygame.display.set_mode((800,800))
window.fill(BACKGROUND_COLOR)

#Draw the grid
pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(265, 50, 5, 700))
pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(532, 50, 5, 700))
pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(50, 265, 700, 5))
pygame.draw.rect(window, FOREGROUND_COLOR, pygame.Rect(50, 532, 700, 5))

#take in game parameters

#start the game (while loop)
    #draw board
    #player1 makes move
    #check for win
    #draw board
    #player2 makes move
    #check for win

#MAIN LOOP
choices=["X","O"]
game=0
while game==0:
    start=int(input("Select the amount of players (1 or 2):"))
    if start==1:
        def random():
            import random
            print(random.choice(choices))
        random()
            
        
    
    #Detect mouse click or closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            _ = pygame.mouse.get_pos()
    
    #Draw X or O
    draw('x', 0)
    draw('o', 4)
    draw('x', 8)

    #Draw a new frame each time the program loops
    pygame.display.update()
    clock.tick(60) 
