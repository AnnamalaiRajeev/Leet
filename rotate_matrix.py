

def rotate(matirx, n):
    k=0
    while k < n:
        for i in range(len(matirx)):
            for j in range(i, len(matirx)):
                matirx[i][j], matirx[j][i] = matirx[j][i], matirx[i][j]

        for i in range(len(matirx)):
            for j in range(len(matirx)//2):
                matirx[i][j], matirx[i][len(matirx)-1-j] = matirx[i][len(matirx)-1-j], matirx[i][j]
        k+=1


    return matirx

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
y = rotate(a,3)
print(y)