'''
🔹 Q5: Find the First Non-Repeating Character in a String

Question:
Given "aabbccdeff", return "d".

Theory Used:

Requires hashing + frequency count.

Dictionaries in Python maintain insertion order (since Python 3.7).

Internal Working:

dict is implemented as a hash table with open addressing.

Counting is O(n) because lookup/update in dict is amortized O(1).
'''

def first_non_repeating(s:str) -> str :
    freq = {}
    for ch in s :
        freq [ch] = freq.get(ch, 0) + 1
    for ch in s :
        if freq[ch] == 1 :
            return ch
    return None

print(first_non_repeating("aaaabbbbssscdecdechuk"))