'''
Q3. Hard – Subarray with Given Sum (Sliding Window)
'''

def subarray_sum(num, target):
    left = 0
    total = 0
    for right , val in enumerate(num):
        total += val
        while total > target:
            total -= num[left]
            left +=1
        if total == target:
            return (left, right)
    return None

print(subarray_sum([1,2,3,7,5], 12)) 