'''
🔹 Q12: Flatten a Nested List

Question:
[[1, 2], [3, [4, 5]]] → [1, 2, 3, 4, 5].

Theory:

Requires recursion (stack-based expansion).

Internal Working:

Python recursion creates new stack frames in C for each call.
'''

def flatten(lst) :
    result = []
    
    for item in lst :
        if isinstance(item ,list) :
            result.extend(flatten(item))
        else :
            result.append(item)
    return result

print(flatten([[1, 2], [3, [4, 5]]]))