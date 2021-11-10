#Import dependencies
import random
import matplotlib
import pygame

#A function that draws the game board to the screen
def draw():
    #A list of the coordinates of the top left corner of each space
    SPACES = [(50, -100), (300, -100), (550, -100), (50, 150), (300, 150), (550, 150), (50, 400), (300, 400), (550, 400)]
    
    #Loop through the "board" and draw every character in the right space
    for i in range(9):
        text = FONT.render(board[i], True, FOREGROUND_COLOR)
        window.blit(text, SPACES[i])

#Takes in x, y coordinates and returns the space number that those coordinates are in
def coordsToSpace(position):
    #A list of the coordinates of the top left and bottom right corners of each space
    SPACES = [((0, 0),(265, 265)), ((265, 0),(532, 265)), ((532, 0),(800, 265)), ((0, 265),(265, 532)), ((265, 265),(532, 532)), ((532, 265),(800, 532)), ((0, 532),(265, 800)), ((265, 532),(532, 800)), ((532, 532),(800, 800))]
    
    #Loop through every space, check if the x coordinate is in the space, check if the y coordinate is in the space, return the space number
    for i in range(9):
        if position[0] >= SPACES[i][0][0] and position[0] < SPACES[i][1][0]:
            if position[1] >= SPACES[i][0][1] and position[1] < SPACES[i][1][1]:
                return i

#Create a game board
board = ['x', '', '', '', 'x', '', '', '', 'x'] #This is just for testing

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
            clickPosition = pygame.mouse.get_pos()
            print(coordsToSpace(clickPosition))
    
    #Draw X or O
    draw()

    #Draw a new frame each time the program loops
    pygame.display.update()
    clock.tick(60) 
