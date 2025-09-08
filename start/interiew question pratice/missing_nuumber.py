'''
🔹 Q7: Find Missing Number in 1 to N

Question:
Input: [1, 2, 4, 5], Output: 3.

Theory:

Uses arithmetic progression formula:
Sum of 1…n = n(n+1)/2.

Compare with actual sum.

Internal Working:

sum() in Python is a C loop that avoids Python function calls, making it very fast.
'''

# def missing_number(nums) :
#     n = len(nums) + 1
#     total = n * (n + 1 ) // 2
#     return total - sum(nums)

# print(missing_number([1,2,3,4,6]))

def missing_numbers(nums, N) :
    full_set = set(range(1, N+1))  # all numbers from 1 to N
    nums_set = set(nums)  # numbers present in input
    
    missing = sorted(list(full_set - nums_set))  # get missing numbers
    
    return missing

print(missing_numbers([1,2,5], 5))     
print(missing_numbers([1,2,3,5], 5))
print(missing_numbers([2,3,7,1], 7))  
    