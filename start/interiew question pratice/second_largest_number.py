
'''
🔹 Q8: Find Second Largest Number

Question:
Given [10, 5, 20, 8], find 10.

Theory:

Requires linear scan or sorting.

Sorting: O(n log n), One-pass: O(n).

Internal Working:

Python’s max() is a loop in C.

Sorting uses Timsort.
'''

# def second_largest_number(nums):
#     nums = list(set(nums))
#     nums.sort(reverse=True)
#     if (len(nums)  < 2) :
#         return None
#     return nums[1]

# ! TOC O(n)
def second_largest_number(nums):
    first = second = float('-inf')  # ? -inf -> negative infinity
    for n in nums :
        if n > first :
            second = first
            first = n 
        elif first > n > second :
            second = n
    return second if second != float('-inf') else None

print(second_largest_number([10,15,11,8]))