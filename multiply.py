def recursice_multiply(a, b):
    
    if a == 0 or b == 0:
        return 0
    if b < 0:
        return -recursice_multiply(a, -b)
    
    return a + recursice_multiply(a, b - 1)


num1 = 2
num2 = 3
result = recursice_multiply(num1, num2)
print(f"{num1} * {num2} = {result}")
    
    
    