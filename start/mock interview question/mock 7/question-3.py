'''
Q3. Hard – Maximum Product Subarray
'''

def max_product(nums):
    res = cur_max = cur_min = nums[0]
    
    for n in nums[1:]:
        temp = cur_max
        cur_max = max(n ,n*cur_max, n*cur_min)
        cur_min = min(n ,n*temp, n*cur_min)
        res = max(res, cur_max)
    return res
        
print(max_product([2,3,-2,4]))
