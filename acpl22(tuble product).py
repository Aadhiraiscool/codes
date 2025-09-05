def multiple_tuple(nums):
    temp=list(nums)
    prod=1
    for item in temp:
        prod=prod*item
    return prod
nums=(1,2,3,4,5,6,7)
print("original tuple")
print(nums)

print("product of all elements of the tuple",multiple_tuple(nums))
    
