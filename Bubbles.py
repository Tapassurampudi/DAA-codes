def letters_numbers(number_str):
    letter_mapping = {
        '1': '000',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqr',
        '8': 'stu',
        '9': 'vwx'
    }

    combinations = ['']

    for digit in number_str:
        if digit in letter_mapping:
            new_combinations = []
            for letter in letter_mapping[digit]:
                for combination in combinations:
                    new_combinations.append(combination + letter)
            combinations = new_combinations

    return combinations

number_str = input("Enter a string of digits (0-9): ")
combinations = letters_numbers(number_str)
print(combinations)