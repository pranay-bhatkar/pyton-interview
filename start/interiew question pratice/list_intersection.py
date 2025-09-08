'''
Question:
[1, 2, 3, 4] and [3, 4, 5] → [3, 4].

Theory:

Uses set intersection.

Internal Working:

Set operations use bitwise hash table checks → O(min(n, m)).
'''
def list_intersection(a,b) :
    return list (set(a) & set(b))

print(list_intersection([1,3,2],[1,5]))