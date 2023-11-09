matrix = [
    [1, 3, 2],
    [9, 4, 12],
    [6, 8, 18]
]

divisible_by_3 = []

for row in matrix:
    for num in row:
        if num % 3 == 0:
            divisible_by_3.append(num)

product = 1
for num in divisible_by_3:
    product *= num


if product > 50:
    print("Product of divisible-by-3 numbers:",divisible_by_3,product)
else:
    print("Product is not greater than 50.")