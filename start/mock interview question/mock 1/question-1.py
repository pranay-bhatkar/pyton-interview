'''
Q1. Easy – Check if a string is a palindrome ignoring cases and spaces
'''

def is_palindrome(s:str) -> bool:
    s =  "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("python"))

