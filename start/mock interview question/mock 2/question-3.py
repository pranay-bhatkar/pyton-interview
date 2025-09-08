'''
Q3. Hard – Longest Palindromic Substring
'''

def longest_palindrome(s:str) -> str:
    res = ""
    for i in range(len(s)):
        l , r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(res):
                res = s[l:r+1]
            l -= 1 
            r += 1
            
        # even length
        l , r = i , i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(res):
                res = s[l:r+1]
            l -= 1; r += 1
    return res

print(longest_palindrome("babad"))  # "bab" or "aba"

                