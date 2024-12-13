# 4. Create a function that takes a list of integers and returns the sum of all even numbers.
def STnum (nums):
    list= []
    for i in range (0,len(nums)):
        if nums[i] % 2 == 0 :
            list.append(nums[i])
        
    sum=0
    for i in range (0,len(list)):
        sum += list[i]
    return sum

kyun= [1,2,3,4,5,6,7,8,9,0]
print(STnum(kyun))