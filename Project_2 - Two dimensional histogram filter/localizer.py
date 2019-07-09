import pdb
from helpers import normalize, blur
import copy

def initialize_beliefs(grid):
    """
    Fill grid with intializ beliefs (continious distribution)
    """
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    """
    Sense location of robot based on the given beliefs and current 
    "measured" value multipling the given p_hit or p_miss values. 
    """
    new_beliefs = copy.deepcopy(beliefs)

    for rowIndex in range(len(grid)):
        for colIndex in range(len(grid[rowIndex])):
            if grid[rowIndex][colIndex] == color:
                new_beliefs[rowIndex][colIndex] = beliefs[rowIndex][colIndex] * p_hit
            else:
                new_beliefs[rowIndex][colIndex] = beliefs[rowIndex][colIndex] * p_miss
    return normalize(new_beliefs)
    #
    # TODO - implement this in part 2
    #

    return new_beliefs

def normalize(beliefs):
    """
    Normalize beliefs-2d-array to ensure the sum of all given values is equal to 1.
    normalizedValue = currValue / sumOfAllValues 
    """
    normalized = copy.deepcopy(beliefs)
    allSum = 0
    for i in range(len(beliefs)):
        allSum += sum(beliefs[i])
        
    for rowIndex in range(len(beliefs)):
        for colIndex in range(len(beliefs[rowIndex])):
            normalized[rowIndex][colIndex] = beliefs[rowIndex][colIndex] / allSum
    return normalized
                   

def move(dy, dx, beliefs, blurring):
    """
    Move the object in the 2d-grid by dx (delta x) and dy (delta y).
    Afterward recaluclate the beliefs in account of the blurring which 
    takes effect when moving through the grid. 
    (Move increase the uncertainity about the position) 
    """
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            # new_i is row (% height)
            # new_j is column (% width)
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)