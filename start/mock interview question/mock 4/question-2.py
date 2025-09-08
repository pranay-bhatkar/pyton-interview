'''
Q2. Medium – Find Missing Number (1 to n)
'''

def missing_number(nums):
    n = len(nums) + 1
    expected = n * (n+1) // 2
    return expected - sum(nums)

print(missing_number([1,2,4,5]))