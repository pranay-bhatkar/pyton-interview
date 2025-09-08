'''
Q2. Medium – Find the Majority Element (> n/2 times)
'''

def majority_element(nums):
    count , candidate = 0, None
    for num in nums :
        if count == 0 :
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

print(majority_element([2,2,1,1,1,2,2]))