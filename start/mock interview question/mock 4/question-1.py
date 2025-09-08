'''
Q1. Easy – Find Factorial
'''

def facttorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(facttorial(3))