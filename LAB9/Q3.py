N = int(input("Enter the value of N: "))
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
print(f'Matrix: {matrix}')
is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(N) for j in range(N))
print("Symmetric" if is_symmetric else "Not Symmetric")
principal_diagonal_sum = sum(matrix[i][i] for i in range(N))
non_principal_diagonal_sum = sum(matrix[i][N-i-1] for i in range(N))

print("Sum of Principal Diagonal elements:", principal_diagonal_sum)

print("Sum of Non-Principal Diagonal elements:", non_principal_diagonal_sum)

is_upper_triangular = all(matrix[i][j] == 0 for i in range(1, N) for j in range(i))

is_lower_triangular = all(matrix[i][j] == 0 for i in range(N) for j in range(i+1, N))

print("Upper Triangular" if is_upper_triangular else "Not Upper Triangular")

print("Lower Triangular" if is_lower_triangular else "Not Lower Triangular")

transpose = [[matrix[j][i] for j in range(N)] for i in range(N)]

print("Transpose of the matrix:")
for row in transpose:
    print(' '.join(map(str, row)))
