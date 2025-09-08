'''
🔹 Q6: Anagram Check

Question:
Check if two strings are anagrams ("listen" and "silent").

Theory:

Anagrams → same characters, same frequency.

Requires sorting or hash maps.

Internal Working:

sorted() internally uses Timsort (hybrid of merge + insertion sort).

collections.Counter uses a dictionary with character frequency.
'''

# ! TOC O(n log n)

# ? Sorting
# def is_anagram(s1 :str,s2: str) -> bool :
#     result = sorted(s1) == sorted(s2)
#     return result

# print(is_anagram("listen", "silent"))

# ! TOC O(n)
# ? Frequency Count (Dictionary / Counter)
# from collections import Counter

# def is_anagram(s1:str, s2:str) -> bool :
#     return Counter(s1) == Counter(s2)

# print(is_anagram("listen", "silent"))


# ! TOC O(n)
# ? Manual Hash Map (No imports)
# def is_anagram(s1,s2) :
#     if len(s1) !=  len(s2) :
#         return False
    
#     freq = {}
#     for ch in s1 :
#         freq[ch] = freq.get(ch, 0) + 1 
    
#     for ch in s2 :
#         if ch not in freq :
#             return False
        
#         freq[ch] = freq[ch] - 1
        
#         if (freq[ch] < 0) :
#             return False
    
#     return all(v == 0 for v in freq.values())

# print(is_anagram("listen", "enlist"))


from itertools import permutations

def all_anagrams(word: str):
    #  # Use set to remove duplicate letters in the word first
    # letters = set(word)
    
    # # Generate permutations of the unique letters
    # perms = permutations(letters)
    
    # Generate all permutations
    perms = permutations(word)
    
    # Convert each tuple to string and use set to remove duplicates
    unique_anagrams = set(''.join(p) for p in perms)
    
    print(f"Total anagrams: {len(unique_anagrams)}")
    print("Anagrams:")
    for anagram in unique_anagrams:
        print(anagram)

# Example
all_anagrams("listen")
