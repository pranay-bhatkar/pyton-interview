'''
🔹 Q14: Find Majority Element (> n/2 times)

Question:
Input [2, 2, 1, 2, 3, 2, 2] → 2.

Theory:

Use Boyer–Moore Voting Algorithm.

Internal Working:

Only one pass, no extra space.

Works by canceling out elements.
'''

def majority_element(num) :
    count = 0
    candidate = None
    for i in num:
        if count == 0:
            candidate = i
        count += (1 if i == candidate else -1)
    return candidate

print(majority_element([2, 2, 1, 2, 3, 2, 2]))