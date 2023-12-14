def highest_consonant_value(s):
    vowels = "aeiou"
    max_value = 0
    current_value = 0

    for char in s:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    # Check one last time in case the string ends with a consonant substring
    max_value = max(max_value, current_value)

    return max_value


input_string = "abcde"
result = highest_consonant_value(input_string)
print(result)