# 5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.he greatest common factor number that divides them, exactly
def GCD (a,b):
    a_list = []
    b_list = []
    c= []
    for i in range (1,a):
        if a % i == 0:
            a_list.append(i)
        
    for i in range (1,b):
        if b % i == 0:
            b_list.append(i)
    for i in range(0,len(a_list)):
        for j in range(0,len(b_list)):
            if a_list[i] == b_list[j] :
                c.append(a_list[i])
    c.sort()
    return c[len(c) - 1]
g= int(input("please enter first number: "))
h= int(input("please enter second number: "))
print(GCD (g,h))