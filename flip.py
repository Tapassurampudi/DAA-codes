def update_boundary_to_1(matrix):
    if not matrix:
        return matrix

    
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_cols):
        matrix[0][i] = 1
        matrix[num_rows - 1][i] = 1

    for i in range(1, num_rows - 1):
        matrix[i][0] = 1
        matrix[i][num_cols - 1] = 1

    return matrix


matrix = [
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]


updated_matrix = update_boundary_to_1(matrix)


for row in updated_matrix:
    print(row)