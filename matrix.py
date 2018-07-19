import random
from copy import deepcopy

class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        
        self.rows = nrows
        self.cols = ncols
        self.matrix = list()
        for i in range(0,self.rows):
            matrix = list()
            for j in range(0,self.cols):
                matrix.append(random.randint(0,9))
            self.matrix.append(matrix)
            
    def add(self, m):
        """return a new Matrix object after summation"""
        result = Matrix(self.rows, self.cols)
        if self.rows == self.cols:
            for i in range(0,self.rows):
                for j in range(0, self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
            return result
        else :
            print('Matrix size should in the same size!! ')
            return None

    def sub(self, m):
        """return a new Matrix object after substraction"""
        result = Matrix(self.rows, self.cols)
        if self.rows == self.cols:
            for i in range(0,self.rows):
                for j in range(0,self.cols):
                    result.matrix[i][j] = self.matrix[i][j] - m.matrix[i][j]
            return result
        else :
            print('Matrix size should in the same size!! ')

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        
        result = Matrix(self.rows, m.cols)
        for i in range(0,len(self.matrix)):
            for j in range(0,len(m.matrix[0])):
                result.matrix[i][j] = 0
                for p in range(0,len(self.matrix[0])):
                    result.matrix[i][j] = result.matrix[i][j] + self.matrix[i][p] * m.matrix[p][j]
        return result

    def transpose(self):
        """return a new Matrix object after transpose"""
        '''
        self.matrix[0][1] , self.matrix[1][0] = self.matrix[1][0] , self.matrix[0][1] 
        self.matrix[0][2] , self.matrix[2][0] = self.matrix[2][0] , self.matrix[0][2] 
        self.matrix[1][2] , self.matrix[2][1] = self.matrix[2][1] , self.matrix[1][2] 
        '''
        result = Matrix(self.rows, self.cols)
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                result.matrix[j][i] = self.matrix[i][j] 
        return result
      
    def display(self):
        """Display the content in the matrix"""
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                print(self.matrix[i][j],end=' ')
                j +=1
            i +=1
            print('')
    
A_row = int(input("Enter A matrix's rows : "))
A_col = int(input("Enter A matrix's cols : "))
A_matrix = Matrix(A_row,A_col)
A_matrix.display()
print('')
B_row = int(input("Enter B matrix's rows : "))
B_col = int(input("Enter B matrix's cols : "))
B_matrix = Matrix(B_row,B_col)
B_matrix.display()
print('=====A + B=====')
C = A_matrix.add(B_matrix)
if C != None:
    C.display()
print('=====A - B=====')
C = A_matrix.sub(B_matrix)
if C != None:
    C.display()
print('=====A * B=====')
C = A_matrix.mul(B_matrix)
C.display()
print('=====tran A * B=====')
C = C.transpose()
C.display()
# A = Matrix(3, 3)
# B = Matrix(3, 3)
# C = A.add(B)
# C.display()

