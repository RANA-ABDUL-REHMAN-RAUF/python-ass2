
# Intermediate Function Questions

# 1. Create a function that takes a list of numbers and returns the largest number.
def Hnum (nums):
    nums=sorted(nums)
    return nums[len(nums) - 1]

ko= [123,4567,890,23456,887654,56]
print(Hnum(ko))