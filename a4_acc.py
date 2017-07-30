# a4 accessories
# Louis Liu and Daisy Fan


#STUDENTS: DO NOT ALTER THIS MODULE

class Game(object):
    """A board on which Conway's Game of Life is played.
        
        Instance Attributes:
            height [int]: number of rows in the gameboard
            
            width [int]: number of columns of the gameboard
            
            board [height x width nested list of ints]:
                    the nested list to represent the gameboard.
                    The stored values are 0 and 1 to represent "dead"
                    and "alive", respectively.
            
            seedlist [List of 2-int lists or None]:
                    a list representing the coordinates of the initally "alive"
                    cells.  If seedlist is None then the intial game board has
                    randomly generated "alive" cells
    """
    