matrix = [
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
]

max_count = 0  
max_row = -1
for i in range(len(matrix)):
    count = matrix[i].count(1)  
    if count > max_count:
        max_count = count
        max_row = i


if max_row != -1:
    print(f"The row with the most 1s is row {max_row} with {max_count} 1s.")
else:
    print("No row contains 1s in the matrix.")
