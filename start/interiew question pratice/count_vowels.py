'''
🔹 Q9: Count Vowels in a String

Question:
Count vowels in "Interview".

Theory:

Uses set membership for O(1) lookup.

Internal Working:

in operator checks hash table for sets.

String iteration is O(n) over Unicode code points.
'''

def count_vowels(s:str) -> int :
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)

print(count_vowels("pranay"))
    