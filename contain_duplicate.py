def duplicate(nums):
    num_set=set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False
nums=[1,2,3,1]
print(duplicate(nums))
