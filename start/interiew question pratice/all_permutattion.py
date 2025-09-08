'''
🔹 Q15: Find All Permutations of a String

Question:
Input "abc", Output ["abc", "acb", "bac", "bca", "cab", "cba"].

Theory:

Uses recursion + backtracking.

Alternatively, itertools.permutations.

Internal Working:

itertools.permutations generates results lazily → saves memory.
'''
from itertools import permutations

def all_permutation(s) :
    return["".join(p) for p in permutations(s)]

print(all_permutation("abc"))