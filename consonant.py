# Function to check if a character is a consonant
def is_consonant(char):
    return char.isalpha() and char not in "aeiou"

# Function to calculate the value of a consonant
def get_consonant_value(char):
    return ord(char) - ord('a') + 1

# Function to find the highest consonant value in a string
def highest_consonant_value(s):
    max_value = 0
    current_value = 0

    for char in s:
        if is_consonant(char):
            current_value += get_consonant_value(char)
            max_value = max(max_value, current_value)
        else:
            current_value = 0

    return max_value

# Example usage
input_string = "joyce"
result = highest_consonant_value(input_string)
print("Highest consonant value in the input string:", result)
