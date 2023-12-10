N = int(input("Enter the value of N: "))
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
print(f'Matrix: {matrix}')



lead = 0
rowCount = len(matrix)
columnCount = len(matrix[0])

for r in range(rowCount):
    if lead >= columnCount:
        break
    i = r
    while matrix[i][lead] == 0:
        i += 1
        if i == rowCount:
            i = r
            lead += 1
            if columnCount == lead:
                break
    matrix[i], matrix[r] = matrix[r], matrix[i]
    lv = matrix[r][lead]
    matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
    for i in range(rowCount):
        if i != r:
            lv = matrix[i][lead]
            matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
    lead += 1
