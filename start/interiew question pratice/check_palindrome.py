'''
Question:
Check if "madam" is a palindrome.

Theory Used:

A palindrome reads the same forwards and backwards.

Requires knowledge of string indexing.

Internal Working:

Indexing uses PyUnicode_Substring to fetch characters.

Comparing s[i] with s[-i-1] involves accessing Unicode code points.
'''

str = input("enter the string to check it is palindrome or not :")

def is_palindrome() -> bool :
    return str == str[::-1]

print(is_palindrome())
