# 6. Write a function to count the vowels in a given string.
def Vcounter(string):
    count=0
    string=string.lower()
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    return count
