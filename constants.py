# a4 game constants
# Louis Liu and Daisy Fan


# Representation of a grid square's status
ALIVE = 1
DEAD = 0

# Number of game iterations
STEPS = 80

# Fun seedlist shapes :)
# A seedlist is a list of coordinates in [x,y] form.  The positions in a
# seedlist are the only positions that have the value ALIVE in the gameboard
# at the initial state.  An [x,y] position maps to column x and row y of the
# game board.  Coordinates must be non-negative.  x and y values must be less
# than WIDTH and HEIGHT, respectively.
GLIDER_GUN =  [[1,5],[1,6],[2,5],[2,6],[11,5],[11,6],[11,7],[12,4],[12,8],[13,3],
    [13,9],[14,3],[14,9],[15,6],[16,4],[16,8],[17,5],[17,6],[17,7],[18,6],[21,3],
    [21,4],[21,5],[22,3],[22,4],[22,5],[23,2],[23,6],[25,1],[25,2],[25,6],[25,7],
    [35,3],[35,4],[36,3],[36,4]]
########
[[]]


# TO DO:
# Make two other seedlists.  Search online for seedlists that result in
# interesting patterns in Conway's Game of Life simulation or create your own!


# Board constants
HEIGHT = 25
WIDTH = 40
SEEDLIST = None # Should be a list of list coordinates in [x,y] form.
#SEEDLIST= None  # Set to None if random initial pattern is to be used.
SEED_COUNT = (HEIGHT*WIDTH)/4  # Maximum number of positions with the value
                               # ALIVE if SEEDLIST is None

# Graphics
SHOW_GRAPHICS = True  # Set to True after you implement a4.makeBoard and
                       # a4.setup
BLINK = 0.1  # Time in seconds between graphics updates



        
        
    
    
    