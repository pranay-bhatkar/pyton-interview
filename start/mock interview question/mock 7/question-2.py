'''
Q2. Medium – Find Intersection of Two Arrays
'''

def intersection(num1, num2):
    return list(set(num1) & set(num2))

print(intersection([1,2,2,1],[2,2]))