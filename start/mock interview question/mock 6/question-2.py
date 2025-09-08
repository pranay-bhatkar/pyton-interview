'''
Q2. Medium – Rotate Array by k Steps
'''

def rotate(nums, k):
    sorted(nums)
    k %= len(nums)
    return nums[-k:] + nums[:-k]

print(rotate([1,3,2,4,5,6,7], 3)) 