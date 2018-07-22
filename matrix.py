import random

from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.n = nrows
        self.matrix = [[random.randint(0,9) for i in range(self.n)] for j in range(self.n)]
        

    def add(self, m):
        """return a new Matrix object after summation"""
        data1 = [[0 for col in range(self.n)] for row in range(self.n)] #a+b
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                data1[i][j] = m[i][j] + self.matrix[i][j]
        print("x + y:",data1)

    def sub(self, m):
        """return a new Matrix object after substraction"""
        data2 = [[0 for col in range(self.n)] for row in range(self.n)] #a-b
        for i in range(len(m)):
            for j in range(len(m[i])):
                data2[i][j] = - m[i][j] + (self.matrix[i][j])
        print("x - y:",data2)

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        data3 = [[sum(x * y for x, y in zip(x, y)) for y in zip(*m)] for x in self.matrix]
        print("x * y:",data3)

    def transpose(self):
        """return a new Matrix object after transpose"""
        print (list(map(list, zip(*self.matrix))))
    
    
    def display(self):
        """Display the content in the matrix"""
        print(self.matrix)


x = Matrix(4,4)
y = Matrix(4,4)
print(x.matrix)
print(y.matrix)
x.add(y.matrix)
x.sub(y.matrix)
x.mul(y.matrix)
x.transpose()
y.transpose()
x.display()
y.display()
