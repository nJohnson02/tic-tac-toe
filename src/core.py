"""
Tic-Tac-Toe
By: Nathan, Margret, Jasmine, and Madison

A python tic-tac-toe game using pygame!

"""

#Import dependencies
import random
import matplotlib.pyplot as plt
import pygame


#A function that draws the game board to the screen
def draw():
    #A list of the coordinates of the top left corner of each space
    SPACES = [(50, -100), (300, -100), (550, -100), (50, 150), (300, 150), (550, 150), (50, 400), (300, 400), (550, 400)]
    
    #Loop through the "board" and draw every character in the right space
    for i in range(len(SPACES)):
        text = FONT.render(board[i], True, FOREGROUND_COLOR)
        WINDOW.blit(text, SPACES[i])

    #Update pygame to show the new changes
    pygame.display.update()


#Takes in x, y coordinates and returns the space number that those coordinates are in
def coordsToSpace(position):
    #A list of the coordinates of the top left and bottom right corners of each space
    SPACES = [((0, 0),(265, 265)), ((265, 0),(532, 265)), ((532, 0),(800, 265)), ((0, 265),(265, 532)), ((265, 265),(532, 532)), ((532, 265),(800, 532)), ((0, 532),(265, 800)), ((265, 532),(532, 800)), ((532, 532),(800, 800))]
    
    #Loop through every space, check if the x coordinate is in the space, check if the y coordinate is in the space, return the space number
    for i in range(len(SPACES)):
        if position[0] >= SPACES[i][0][0] and position[0] < SPACES[i][1][0]:
            if position[1] >= SPACES[i][0][1] and position[1] < SPACES[i][1][1]:
                return i

        
#Function that will return True if someone has won the game and Flase otherwise
def checkForWin():
    #List of all possible rows of 3
    POSSIBLE_WINS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    
    #Loop through every possible row of 3, if all 3 spaces in any row of 3 are the same symbol, someone has won the game
    for row in POSSIBLE_WINS:
        if board[row[0]] == PLAYER_SYMBOL and board[row[1]] == PLAYER_SYMBOL and board[row[2]] == PLAYER_SYMBOL:
            print("Congrats, you won!")
            playerStats[0]=playerStats[0]+1
            return True
        elif board[row[0]] == AI_SYMBOL and board[row[1]] == AI_SYMBOL and board[row[2]] == AI_SYMBOL:
            print("You lost. Better luck next time.")
            playerStats[1]=playerStats[1]+1
            return True
            
    #Loop through every space to check for a tie
    for space in board:
        if space == "":
            return False
    playerStats[2]=playerStats[2]+1
    print("No more spaces available. Game over.")
    return True


#Wait for the player to make a move
def playerMove():
    waiting = True
    while waiting:
        #Detect mouse click or closed WINDOW
        for event in pygame.event.get():
            # End program if the "x" button on pygame WINDOW is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Detect if the player clicks on a space
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickPosition = pygame.mouse.get_pos()
                clickSpace = coordsToSpace(clickPosition)
                #Make sure the clicked space is empty
                if board[clickSpace]=='':
                    waiting=False
    
    #Put the player's peice in the clicked space
    board[clickSpace] = PLAYER_SYMBOL


#The "ai" opponent makes a move
def aiMove():
    #Choose a random space, if it is empty move there, if not try again.
    space = ''
    while space == '':
        randomNumber = random.randint(0,8)
        if board[randomNumber]=='':
            space = randomNumber
            board[space]=AI_SYMBOL


#If the file exists, read it into playerStats list, otherwise set it to '0','0','0'
try:
    f = open("player_progress.txt", "r")
    playerStats = f.read().split(',')
    f.close()
except:
    playerStats = [0, 0, 0]

#Don't break everything if the file is empty
if len(playerStats) != 3:
    playerStats = [0, 0, 0]

#Make sure the list contains only integers
for i in range(len(playerStats)):
    playerStats[i]=int(playerStats[i])
            
#Create a game board
board = ['', '', '', '', '', '', '',  '', '']

#Ask the player if they want to be X or O
PLAYER_SYMBOL = ''
while PLAYER_SYMBOL != 'x' and PLAYER_SYMBOL != 'o':    
    PLAYER_SYMBOL = input("Please choose an x or an o: ")
    PLAYER_SYMBOL = PLAYER_SYMBOL.lower()

#Set the ai to be the opposite symbol of the player
if PLAYER_SYMBOL == 'x':
    AI_SYMBOL = 'o'
else:
    AI_SYMBOL = 'x'

#Initialize pygame
pygame.init()

#Define constants for colors and fonts
BACKGROUND_COLOR = '#000F00'
FOREGROUND_COLOR = '#13A10E'
FONT = pygame.font.SysFont('arialBlack', 300)

#Create window
pygame.display.set_caption('Tic Tac Toe!')
WINDOW = pygame.display.set_mode((800,800))
WINDOW.fill(BACKGROUND_COLOR)

#Create the grid
pygame.draw.rect(WINDOW, FOREGROUND_COLOR, pygame.Rect(265, 50, 5, 700))
pygame.draw.rect(WINDOW, FOREGROUND_COLOR, pygame.Rect(532, 50, 5, 700))
pygame.draw.rect(WINDOW, FOREGROUND_COLOR, pygame.Rect(50, 265, 700, 5))
pygame.draw.rect(WINDOW, FOREGROUND_COLOR, pygame.Rect(50, 532, 700, 5))

#Draw the grid to the screen
pygame.display.update()


#MAIN LOOP
while True:

    #The computer makes a move, draw the board, check for win
    print("Computer move.")
    aiMove()
    draw()
    if checkForWin() == True:
        break

    #Wait for the player to make a move, draw the board, check for win
    print("Player one move.")
    playerMove()
    draw()
    if checkForWin() == True:
        break
    

#Close the pygame window when the game is done
pygame.quit()

#Writes the updated list of wins, losses, and ties to the file
f = open("player_progress.txt", "w+")
f.write(str(playerStats[0]) +','+ str(playerStats[1]) +','+ str(playerStats[2]))
f.close()

#Generates a pie chart that shows the wins, losses, and draws of the player
labels = ["Wins","Losses","Draws"]
sizes = playerStats
colors = ["#f6ea7bff","#e683a9ff","#ffba52ff"]
plt.pie(sizes, labels=labels, colors=colors)
plt.axis("equal")
plt.title("Player Progress")
plt.show()
