#a4 script
#Louis Liu and Daisy Fan


import a4_acc
import constants
import random
import numpy
import matplotlib.pyplot as plt
import warnings


def setup(match):
    """Initializes a "match" of Conway's Game of Life. Sets the match's height,
    width, and seedlist attributes, then generates the match's board with
    initially "alive" coordinates given by the match's seedlist.
    If the seedlist has the value None, then set random positions in the board
    to the state constants.ALIVE.  See Assignment 4 description for the
    requirements of random initialization.
    
        :param match: the match to set up
        Precondition: match is an instance of Game
    """
    match.height = constants.HEIGHT
    match.width = constants.WIDTH
    match.board = makeBoard(match.height, match.width)
    match.seedlist = constants.SEEDLIST
    if match.seedlist == None:
        match.seedlist=randseed(match.height, match.width)
    numofrow = len(match.seedlist[0])    #opposite notation because column-major not row-major
    for x in match.seedlist:
        match.board[x[0]][x[1]] = constants.ALIVE
        
        
        
        
    
            
    
    # TO DO:
    # Initialize board according to match.seedlist

def randseed(height, width):
    '''generated a random seedlist with a random number of coordinates but LIMITED to the parameters set with the possible cells existing on the board. Therefore,
    maximum ALIVE positions on a 40*50 board will equal to a total of 500 or less possible start positions.
    
    :param height: number of rows in the board
    :param width: number of columns in the board
    Precondition: height and width are positive ints
    '''
    
    x= width 
    y=height
    result = [] #Accumulator list to gather the coordinates
    seedcount = constants.SEED_COUNT
    num_of_coord = random.randint(1,seedcount)
    for coordinate in range(num_of_coord):
        tempx = random.randint(0,width-1)
        tempy = random.randint(0,height-1)
        coordinate = [tempx, tempy]
        result.append(coordinate)
    return result
            

def makeBoard(height, width):
    """ Returns: a 2D nested list in column-major order representing the game
    board of Conway's Game of Life.  All the cells in the board are in the
    state constants.DEAD.
    
    :param height: number of rows in the board
    :param width: number of columns in the board
    Precondition: height and width are positive ints
    """
    
    result1= []
    
    
    for y in range(width):
        result= [0] * height
        result1.append(result)
        
    return result1
           
              
            
    ########
    # TO DO:
    # Replace the statement below.  Implement this function as specified.
    
    
    


    
def run():
    """Runs a complete match of Conway's Game of Life."""
   
    match = a4_acc.Game() # Instantiate a Game object 
    setup(match)

    if constants.SHOW_GRAPHICS:
        axes= startGraphics(match.board)        #step 0
        
        
    for k in range(constants.STEPS):
        update(match)
        updateGraphics(board, k, caxes)
        
    ########
    # TO DO:    
    # Simulate game given the intial state for constants.STEPS iterations
    
    # Example code to call the updateGraphics function; the second argument
    # needs to be replaced:
    #     if constants.SHOW_GRAPHICS:
    #         updateGraphics(match.board, None, axes) 
    
    # Do not change or add code below here for function run
    endNow= raw_input('Press ENTER to continue.')

    

def update(match):
    """Executes one iteration of a match of Conway's Game of Life.
    Boundary condition: treat the board as though one edge "wraps around"
    to the opposite edge.  See the assignment description for details.
    
    :param match: the match being played
    Precondition: match is an instance of Game
    
    IMPORTANT:
    You must make effective use of at least one "helper function" of your own
    design in completing this function. See the assignment description for
    details."""
    
    
    coordinates= match.board
    
    rows=len(match.board)
    column=len(match.board[0])
    for x in range(rows):
        for y in range(column):
            cell_up = match.board[wrapx(x)][wrapy(y+1)]
            cell_down = match.board[wrapx(x)][wrapy(y-1)]
            cell_right = match.board[wrapx(x+1)][wrapy(y)]
            cell_left = match.board[wrapx(x-1)][wrapy(y)]
            cell_diagupright = match.board[wrapx(x+1)][wrapy(y+1)]
            cell_diagupleft = match.board[wrapx(x-1)][wrapy(y+1)]
            cell_diagdownright = match.board[wrapx(x+1)][wrapy(y-1)] 
            cell_diagdownleft = match.board[wrapx(x-1)][wrapy(y-1)]
    
            listofneightbours = [cell_up, cell_down, cell_right, cell_left, cell_diagupright, cell_diagupleft,
            cell_diagdownright, cell_diagdownleft]
            aliveneighbours = listofneighbours.count(1)
    
            if aliveneighbours < 2:
                x = 0
            elif aliveneighbours == 2:
                x = 1
            elif aliveneighbours == 3:
                x = 1
            else:
                x = 0
    
        
                
def wrapx(x):
    
    
    if x > 40:
        x = 0
    elif x < 0:
        x = 40
    
    
def wrapy(y):    
    if y > 25:
        y = 0
    elif y < 0:
        y = 25
    
    
    ########
    # TO DO:    
    # Implement this function as specified.



########
# TO DO:
# Specify and implement one or more helper functions for update



def updateGraphics(board, step, caxes):
    """Draw the current state of the gameboard.
    Uses the numpy module to convert a Python list to a MATLAB-style array and
    then uses the matplotlib module to produce MATLAB-like graphics.  A cell is
    shown in red if the state is ALIVE or blue if the state is DEAD.
    
    :param board: a 2D nested list storing the state of the gameboard.
    :param step:  An int.  Theiteration number shown in the graphic. The
                  initial state is 0 and the step after the first update is 1,
                  and so on.
    :param caxes: current axes object, which is the gameboard visualization.
    Precondition: board is a column-major order nested list storing zeros and
                  ones """
    boardArray= numpy.transpose(numpy.asarray(board))
    caxes.set_data(boardArray)
    plt.title('Step ' + str(step))
    plt.pause(constants.BLINK)
    plt.show()


def startGraphics(board):
    """ Return: Current axes object for the gameboard.
    Uses the numpy module to convert a Python list to a MATLAB-style array and
    uses the matplotlib module to produce MATLAB-like graphics.
   
    :param board: a 2D nested list storing the state of the gameboard.
    Precondition: board is a column-major order nested list storing zeros and
                  ones """
    plt.ion()
    warnings.filterwarnings("ignore",".*GUI is implemented.*")
    fig= plt.figure(1)
    ax = fig.add_subplot(111)
    caxes= ax.matshow(numpy.transpose(numpy.asarray(board)))
    updateGraphics(board, 0, caxes)
    return caxes


# Script code
run()  # Run the game