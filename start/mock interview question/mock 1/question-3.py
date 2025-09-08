'''
Q3. Hard – Find the longest substring without repeating characters
'''

def longest_unique_substring(s:str) -> int:
    seen = {}
    left = 0
    max_len = 0
    
    for right , ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] +1
        seen[ch] = right
        max_len = max(max_len, right - left+1)
    return max_len

print(longest_unique_substring("abcabcbb"))  
print(longest_unique_substring("bbbbb"))     
print(longest_unique_substring("pwwkew")) 