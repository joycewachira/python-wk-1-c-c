def positive_count(a, b, c):
    # Create a list of positive numbers
    positive_nums = [num for num in (a, b, c) if num > 0]
    
    # Return True if there are at least two positive numbers, otherwise return False
    return len(positive_nums) >= 2

# Example usage
result = positive_count(10, -5, 2)
print(result)
