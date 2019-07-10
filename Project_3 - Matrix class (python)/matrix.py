import math
from math import sqrt
import numbers


def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)

    
def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I
    
    
def getColumn(matrix, columnIndex):
    """
    Returns a specific column (columnIndex) of the given matrix
    """
    # <= because w (width) starts at 1 and index starts at 0
    if (matrix.w <= columnIndex): 
        raise ValueError("Cannot get column " + str(columnIndex) + " - out of range") 

    result = []
    # Iterate through each row and store columnIndex
    for rowIndex in range(len(matrix.g)):
        result.append(matrix.g[rowIndex][columnIndex])
    return result


def getRow(matrix, rowIndex):
    """
    Returns a specific row (rowIndex) of the given matrix
    """
    # <= because h (height) starts at 1 and index starts at 0
    if (matrix.h <= rowIndex): 
        raise ValueError("Cannot get row " + str(rowIndex) + " - out of range") 
    return matrix.g[rowIndex]


def dotProduct(vectorA, vectorB):
    """
    Calculates the dotProduct of two given vectors
    """
    if len(vectorA) != len(vectorB):
        raise ValueError("Vectors cannot have different lengths")
    
    result = []
    for i in range(len(vectorA)):
        result.append(vectorA[i] * vectorB[i])
    return sum(result)

""" 
Matrix class for matrix calculations and object instancing
"""
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise ValueError("Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise NotImplementedError("Calculating determinant not implemented for matrices largerer than 2x2.")
        
        result = []
        
        # 1x1 matrix determinant => 1 / value
        if self.h == 1:
            return self.g[0][0]
        elif self.h == 2: 
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return (a + d) - (c + d)
            

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise ValueError("Cannot calculate the trace of a non-square matrix.")

        result = 0
        for i in range(len(self.g)):
            result += self.g[i][i]
        return result


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise ValueError("Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise NotImplementedError("inversion not implemented for matrices larger than 2x2.")

        result = []
        # Inverse of 1x1 matrix
        if self.h == 1:
            return Matrix([[1 / self.determinant()]])
                    
        # Inverse of 2x2 matrix
        elif self.h == 2:  
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            if (a + d == c + d):
                raise ValueError("Matrix determinant is zero. There will be no matrix inverse")
                
            divider = 1 / ((a * d) - (b * c))
            result.append([d * divider, -(b * divider)])
            result.append([-(c * divider), a * divider])
        return Matrix(result)

        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        result = []
        for columnIndex in range(len(self.g[0])):
            newRow = getColumn(self, columnIndex)
            result.append(newRow)
        return Matrix(result)
        

    def is_square(self):
        return self.h == self.w

    
    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    
    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    
    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be added if the dimensions are the same") 
        
        new_matrix = []
        # Iterate through each row
        for i in range(len(self.g)):
            # Create a new instance of the array after iterating through the columns of a row
            row = []
            # Iterate through each column in row
            for j in range(len(self.g[i])):
                row.append(self.g[i][j] + other.g[i][j])
            new_matrix.append(row)
        return Matrix(new_matrix)

    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        new_matrix = []
        # Iterate through each row
        for i in range(len(self.g)):
            row = []
            # Iterate through each column in row
            for j in range(len(self.g[i])):
                row.append(self.g[i][j] * -1)
            new_matrix.append(row)
        return Matrix(new_matrix)


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be substracted if the dimensions are the same") 
        
        new_matrix = []
        # Iterate through each row
        for i in range(len(self.g)):
            # Create a new instance of the array after iterating through the columns of a row
            row = []
            # Iterate through each column in row
            for j in range(len(self.g[i])):
                row.append(self.g[i][j] - other.g[i][j])
            new_matrix.append(row)
        return Matrix(new_matrix)

    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        result = []
        for i in range(len(self.g)):
            row = getRow(self, i)
            newRow = []
            for j in range(len(other.g[0])):
                newRow.append(dotProduct(getRow(self, i), getColumn(other, j)))
            result.append(newRow)
        return Matrix(result)

    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.
        Multiplies each values of the matrix with the given scalar.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
        result = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[i])):
                row.append(self.g[i][j] * other)
            result.append(row)
        return Matrix(result)