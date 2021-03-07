from display import new_screen, display, save_extension
from draw import add_edge, draw_lines
from matrix import new_matrix, print_matrix, ident, matrix_mult

m1 = [[2, 3, 4], [1, 5, 2]]
m2 = [[1, 2], [4, 6], [8, 4], [7, 3]]

print_matrix(m1)
print_matrix(m2)

id = new_matrix()
ident(id)
print_matrix(id)

print_matrix(matrix_mult(m1, m2))

screen = new_screen()
color = [ 17, 122, 202 ]
matrixLeft = new_matrix(0,0)

add_edge(matrixLeft, 24, 182, 0, 24, 340, 0)
add_edge(matrixLeft, 24, 340, 0, 158, 474, 0)
add_edge(matrixLeft, 158, 474, 0, 158, 182, 0)
add_edge(matrixLeft, 158, 182, 0, 24, 182, 0)

matrixTop = new_matrix(0,0)
add_edge(matrixTop, 182, 340, 0, 182, 474, 0)
add_edge(matrixTop, 182, 474, 0, 340, 474, 0)
add_edge(matrixTop, 340, 474, 0, 474, 340, 0)
add_edge(matrixTop, 474, 340 , 0, 182, 340, 0)

matrixRight = new_matrix(0,0)
add_edge(matrixRight, 340, 316, 0, 474, 316, 0)
add_edge(matrixRight, 474, 316, 0, 474, 158, 0)
add_edge(matrixRight, 474, 158, 0, 340, 24, 0)
add_edge(matrixRight, 340, 24, 0, 340, 316, 0)

matrixBottom = new_matrix(0,0)
add_edge(matrixBottom, 24, 158, 0, 316, 158, 0)
add_edge(matrixBottom, 316, 158, 0, 316, 24, 0)
add_edge(matrixBottom, 316, 24, 0, 158, 24, 0)
add_edge(matrixBottom, 158, 24, 0, 24, 158, 0)

draw_lines( matrixLeft, screen, color )
draw_lines( matrixTop, screen, color )
draw_lines( matrixRight, screen, color )
draw_lines( matrixBottom, screen, color )

display(screen)
save_extension(screen, "pic.png")
