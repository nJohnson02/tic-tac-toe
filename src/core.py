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

    #Update pygame to show the new changes
    pygame.display.update()


#Takes in x, y coordinates and returns the space number that those coordinates are in
def coordsToSpace(position):
    #A list of the coordinates of the top left and bottom right corners of each space
    SPACES = [((0, 0),(265, 265)), ((265, 0),(532, 265)), ((532, 0),(800, 265)), ((0, 265),(265, 532)), ((265, 265),(532, 532)), ((532, 265),(800, 532)), ((0, 532),(265, 800)), ((265, 532),(532, 800)), ((532, 532),(800, 800))]
    
    #Loop through every space, check if the x coordinate is in the space, check if the y coordinate is in the space, return the space number
    for i in range(9):
        if position[0] >= SPACES[i][0][0] and position[0] < SPACES[i][1][0]:
            if position[1] >= SPACES[i][0][1] and position[1] < SPACES[i][1][1]:
                return i


# Wait for the player to make a move
def playerMove():
    clickSpace = ''
    while clickSpace == '':
        #Detect mouse click or closed window
        for event in pygame.event.get():
            # End program if the "x" button on pygame window is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Detect if the player clicks on a space
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickPosition = pygame.mouse.get_pos()
                clickSpace = coordsToSpace(clickPosition)
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


#Function that will return True if someone has won the game and Flase otherwise
def checkForWin():
    #List of all possible rows of 3
    POSSIBLE_WINS=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    
    #Loop through every possible row of 3, if all 3 spaces in any row of 3 are the same symbol, someone has won the game
    for row in POSSIBLE_WINS:
        if board[row[0]] == PLAYER_SYMBOL and board[row[1]] == PLAYER_SYMBOL and board[row[2]] == PLAYER_SYMBOL:
            print("Congrats, you won!")
            return True
        elif board[row[0]] == AI_SYMBOL and board[row[1]] == AI_SYMBOL and board[row[2]] == AI_SYMBOL:
            print("You lost. Better luck next time.")
            return True

    #Loop through every space to check for a tie
    for space in board:
        if space == "":
            return False
    print("No more spaces available. Game over.")
    return True

            
#Create a game board
board = ['', '', '', '', '', '', '',  '', ''] #This is just for testing

#Ask the player if they want to be X or O
PLAYER_SYMBOL = ''
while PLAYER_SYMBOL != 'x' and PLAYER_SYMBOL != 'o':    
    PLAYER_SYMBOL = input("Please choose an x or an o: ")
    PLAYER_SYMBOL = PLAYER_SYMBOL.lower()

#Set the ai to be the opposite symbol of the player
if PLAYER_SYMBOL=="x":
    AI_SYMBOL="o"
else:
    AI_SYMBOL="x"

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


#MAIN LOOP
while True:
    #Draw a new frame each time the program loops
    pygame.display.update()

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
