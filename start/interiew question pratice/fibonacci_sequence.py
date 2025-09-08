'''
🔹 Q4: Implement a Fibonacci Sequence Generator

Question:
Generate the first N Fibonacci numbers.

Theory Used:

Recursion vs Iteration.

Python recursion uses call stack (each call adds a new frame).

Iteration is more efficient due to O(1) memory usage.

Internal Working:

Python function calls are managed in C stack frames.

Iteration avoids stack growth → preferred in interviews.
'''

# Iterative
#  ! TOC O(n)
def fib(num) :
    a, b = 0,1
    result = []
    for i in range(num) :
        result.append(a)
        a , b = b , a + b
    return result

# apprach 2

# def fib(n) :
#     seq = [0, 1]
#     for i in range(2,n) :
#         seq.append(seq[-1] + seq[-2]  )
#     return seq[:n]


#  ! TOC O(n^2)
# Recursive 

def fib (n:int) -> int :
    if n <= 1 :
        return n
    return fib(n-1) + fib(n-2)


print([fib(i) for i in range(10)])