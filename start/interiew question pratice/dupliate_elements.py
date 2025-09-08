'''
🔹 Q2: Find Duplicate Elements in a List

Question:
Given a list of integers, find all elements that appear more than once.

Theory Used:

Lists in Python are dynamic arrays.

Sets provide O(1) average lookup (hashing).

Duplicate detection relies on hash tables.

Internal Working:

set() internally uses a hash table (PySetObject).

Each element’s hash is computed with __hash__() and stored.

On collision, Python uses open addressing for resolution.
'''

def find_duplicateds(num) :
    seen = set()
    duplicates = set()
    for i in num :
        if i in seen :
            duplicates.add(i)
        else :
            seen.add(i)
    return duplicates


print(find_duplicateds([1,2,3,1,2,3,5,4,6,4,8,1,3,5]))

# reversed(find_duplicateds)