# 3. Write a function to check whether a string is a palindrome.a word or group of words that is the same when you read it forwards from the beginning or backwards from the end
def Pstr (string):
    string= str(string)
    if string == string[::-1]:
        return (f"{string} is pelindrome")
    else:
        return (f"{string} is not pelindrome")
    
ho= input("Enter a num or word to check it is palindrome")
print(Pstr(ho))