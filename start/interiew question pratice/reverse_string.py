'''
Q1: Reverse a String without using Slicing

Question:
Write a Python program to reverse a string without using slicing ([::-1]).

Theory Used:

Strings in Python are immutable (cannot be changed after creation).

Reversing requires creating a new string by iterating backwards.

Looping concepts (for/while) or built-in functions (reversed()).

Internal Working:

When you do [::-1], Python creates a new string by traversing the original in reverse using PySequence_GetSlice.

Using loops, Python internally creates a new string object each time characters are concatenated.

'''

name="pranay"
new_str= ""

# ! TOC: O(n^2)
def reverse_string(s:int) -> int :
    result = 0
    for ch in s:
        result = ch + result   # we prepeand 
    return result

print(reverse_string(123))

# ! O(n)
def reverse_string_slicing(s:str) -> str :
    return s[::-1]

print(reverse_string_slicing("yanarp"))
 
 
 