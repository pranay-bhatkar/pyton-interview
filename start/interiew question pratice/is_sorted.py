'''
🔹 Q10: Check if List is Sorted

Question:
Check [1, 2, 3, 4] → True, [3, 1, 2] → False.

Theory:

Use pairwise comparison.

Internal Working:

Python’s all() is a generator-based short-circuit evaluation (stops at first False).
'''
# ! TOC O(n log n)
# def is_sorted(nums) :
#     if nums == sorted(nums):
#         return True
#     else  :
#         return False
    
# print(is_sorted([1,2,4]))

# ! TOC O(n)
def is_sorted(num):
    n = len(num) - 1
    for i in range(n) :
        if num[i] > num[i+1] :
            return False
    return True

print(is_sorted([1,2,4,5]))
