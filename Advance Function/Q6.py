# 6. Create a function that takes a string and counts the frequency of each character.
def count_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency