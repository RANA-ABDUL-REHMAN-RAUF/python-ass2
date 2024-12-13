# 5. Create a function to check if a given number is prime.
def prime_founder(num):
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
print(prime_founder(12))