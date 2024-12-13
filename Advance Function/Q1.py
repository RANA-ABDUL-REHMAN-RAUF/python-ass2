# Advanced Function Questions

# 1. Write a function that calculates the power of a number without using the ** operator.

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result