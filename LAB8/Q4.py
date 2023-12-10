R=int(input("enetr the number of rows:"))
C=int(input("enter number of columns:"))
matrix1=[]
for i in range(R):
    row=[]
    for j in range(C):
        x=float(input("enter the number:"))
        row.append(x)
    matrix1.append(row)

matrix2=[]
for i in range(R):
    row=[]
    for j in range(C):
        x=float(input("enter the number:"))
        row.append(x)
    matrix2.append(row)   

sum_matrix=[]
for i in range(R):
    row=[]
    for j in range(C):
        sum=matrix1[i][j]+matrix2[i][j]
        row.append(sum)
    sum_matrix.append(row)

print("Matrix1")
for i in matrix1:
    print(i)

print("Matrix2")
for i in matrix2:
    print(i)

print("Sum Matrix")
for i in sum_matrix:
    print(i)

#2
R1=int(input("enetr the number of rows for 1st matrix:"))
C1=int(input("enter number of columns for 1st matrix:"))
matrix1=[]
for i in range(R1):
    row=[]
    for j in range(C1):
        x=float(input("enter the number:"))
        row.append(x)
    matrix1.append(row)

R2=int(input("enetr the number of rows for 2nd matrix:"))
C2=int(input("enter number of columns for 2nd matrix:"))
matrix2=[]
for i in range(R2):
    row=[]
    for j in range(C2):
        x=float(input("enter the number:"))
        row.append(x)
    matrix2.append(row)   

if C2==R1:
    multiply_matrix=[]
    for i in range(R1):
        row=[]
        for j in range(C2):
            sum=0
            for k in range(C1):
                sum+=matrix1[i][k]*matrix2[k][j]
            row.append(sum)
        multiply_matrix.append(row) 
else:
    print("invalid input ,cannot multiply a matrix with column of 1st != row of 2nd")       

print("Matrix1")
for i in matrix1:
    print(i)

print("Matrix2")
for i in matrix2:
    print(i)

print("multiply Matrix")
for i in multiply_matrix:
    print(i)

