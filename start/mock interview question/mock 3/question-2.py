'''
Q2. Medium – Two Sum Problem
'''

def two_sum(nums, target) :
    seen = {}
    for i , num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return None

print(two_sum([2,7,11,15], 9))  # (0,1)