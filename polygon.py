_vertices = [[0, 0], [0, 4], [4, 4], [4, 0]]
p =[1, 1]


def is_true(_vertices, p):
    vertices = _vertices
    area_n = 0
    area_square = 16
    for i in range(len(vertices)):
        point_A = vertices[i-1]
        print(point_A)
        point_B = vertices[i]
        print(point_B)
        point_C = p
        A_x = point_A[0]
        A_y = point_A[1]
        B_x = point_B[0]
        B_y = point_B[1]
        C_x = point_C[0]
        c_y = point_C[1]
        print(A_x, A_y, B_x, B_y, C_x, c_y)
        area_n += abs(1/2* ((A_x*(B_y-c_y)) + (B_x*(c_y-A_y)) + (C_x*(A_y - B_y))))
    print(area_n)
    if area_n == area_square:
        return True
    else:
        return False


print(is_true(_vertices, p))

