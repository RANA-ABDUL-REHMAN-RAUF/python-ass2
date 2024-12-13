# 2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

def convert_temperature(temp, unit):
    if unit == "C":
        return (temp * 9/5) + 32
    elif unit == "F":
        return (temp - 32) * 5/9
