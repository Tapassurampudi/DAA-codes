def min_flips(str1, str2):
    if len(str1) != len(str2):
        return -1 

    flips = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            flips += 1

    return flips
string1 = "MOM"
string2 = "MMO"
min_flips = min_flips(string1, string2)

if min_flips != -1:
    print(f"Minimum number of flips required: {min_flips}")
else:
    print("The strings have different lengths and cannot be converted with flips.")
