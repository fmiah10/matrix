"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    text = ''
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            text += (str(matrix[j][i]) + " ")
        print(text + "\n")
        text = ''

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
        matrix[i][i] = 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = []
    for i in range (len(m2)):
        ans = []
        for j in range (len(m1[0])): 
            sum = 0
            for k in range (len (m1)):
                sum += (m1[k][j] * m2[i][k])
            ans.append(sum)
        m3.append(ans)
    m2 = m3
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
