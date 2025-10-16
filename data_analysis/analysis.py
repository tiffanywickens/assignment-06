#Question 4
#!/usr/bin/env python
# Analysis script for QTM 350 Assignment 6

def calculate_factorial(n):
    """Calculate the factorial of n (with an intentional error)."""
    if n == 0:
        return 1
    else:
        # Intentional error: should multiply, not add
        return n + calculate_factorial(n - 1)
    
from data_analysis.analysis import calculate_factorial

print(calculate_factorial(5))

#Question 9
def count_vowels(s):
    """Return the number of vowels in a given string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Data Science Computing")) # Should return 8
