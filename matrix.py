def get_matrix(n):
    matrix=[]
    print("enter the matrix :")
    for i in range(n):
        while True:
            row=list(input(f"{i+1}: ").split())
            if len(row)!=n:
                print("the number of elements is wrong")
                continue
            try:
                row=list(map(float,row))
                break
            except ValueError:
                print("you should enter numbers.")
        matrix.append(row)
    return matrix

def small_matrix(matrix,row,col):
    small=[]
    for i in range(len(matrix)):
        if i==row:
            continue
        new_row=[]
        for j in range(len(matrix)):
            if j==col:
                continue
            new_row.append(matrix[i][j])
        small.append(new_row)
    return small

def determinant(matrix):
    n=len(matrix)
    if n==1:
        return matrix[0][0]
    elif n==2:
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    det=0
    for col in range(n):
        sign=(-1)** col
        sub_matrix=small_matrix(matrix,0,col)
        det+=sign*matrix[0][col]*determinant(sub_matrix)
    return det

def detzero(det):
    if det==0:
        print("determinant is 0 and It doesn't have reverse matrix")

def alhagi_matrix(matrix):
    n=len(matrix)
    alhagi=[]
    for i in range(n):
        row=[]
        for j in range(n):
            small=small_matrix(matrix,i,j)
            reverse=((-1)** (i+j))* determinant(small)
            row.append(reverse)
        alhagi.append(row)
    return alhagi

def tranahade(matrix):
    n=len(matrix)
    result=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(matrix[j][i])
        result.append(row)
    return result

def reverse_matrix(matrix,adj,det):
    n=len(matrix)
    inverse=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(adj[i][j]/det)
        inverse.append(row)
    return inverse


while True:
    n=int(input("please enter numbers row to row(0<n<11):"))
    if 1<=n<=10:
        break
    else:
        print("this number is not acceptable.")
m=get_matrix(n)
print(f"determinant: {determinant(m)}")
det=determinant(m)
if det!=0:
    alhagi=alhagi_matrix(m)
    u=tranahade(alhagi)
    inverse_matrix=reverse_matrix(m,u,det)
    print("reverse matrix:")
    for row in inverse_matrix:
        print(" ".join(map(str,row)))
else:
    detzero(det)