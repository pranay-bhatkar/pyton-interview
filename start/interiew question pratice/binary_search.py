'''
🔹 Q13: Implement Binary Search

Question:
Find 7 in [1, 3, 5, 7, 9].

Theory:

Binary Search works only on sorted arrays.

Time complexity: O(log n).

Internal Working:

Indexing in list is O(1) because Python lists are array-based (PyObject**).
'''

def binary_search(num, target):
    l = 0
    r = len(num) - 1
    
    while l <= r :
        mid = (l + r) // 2
        if num[mid] == target :
            return mid 
        elif num[mid] < target :
            l = mid + 1
        else :
            r = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 1))