numbers = [8,9,16,1]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        print (f"({numbers[i]},{numbers[j]})")