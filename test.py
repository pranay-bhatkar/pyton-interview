# 4. Programs
# (i) Input list from user and arrange in order
nums = list(map(int, input("Enter numbers: ").split()))
print("Sorted list:", sorted(nums))

# (ii) Count characters in string & arrange ascending by frequency
from collections import Counter

s = input("Enter a string: ")
count = Counter(s)
for char, freq in sorted(count.items(), key=lambda x: x[1]):
    print(f"{char}: {freq}")

# (iii) Count vowels in string
s = input("Enter a string: ").lower()
vowels = set("aeiou")
print("Vowel count:", sum(1 for ch in s if ch in vowels))

# (iv) Count digits in input
s = input("Enter text: ")
print("Digit count:", sum(c.isdigit() for c in s))

# (v) Snake & Ladder Pattern

# (Hard, common test problem)

def snakes_and_ladders(n):
    num = n*n
    board = []
    for i in range(n):
        row = list(range(num, num-n, -1))
        if i % 2 == 1:
            row.reverse()
        board.append(row)
        num -= n
    for r in board:
        print(" ".join(map(str, r)))

snakes_and_ladders(5)


# Output (5x5):

# 25 24 23 22 21
# 16 17 18 19 20
# 15 14 13 12 11
# 6  7  8  9  10
# 5  4  3  2  1

# (vi) Decode string → "a4b3c2" → "aaaabbbcc"
s = "a4b3c2"
res = ""
i = 0
while i < len(s):
    char = s[i]
    j = i+1
    num = ""
    while j < len(s) and s[j].isdigit():
        num += s[j]
        j += 1
    res += char * int(num)
    i = j
print(res)

# 5. Take input & count integer values
data = input("Enter values: ").split()
int_count = sum(1 for x in data if x.isdigit())
print("Total integers:", int_count)

# 6. Queue (FIFO) – Enqueue & Dequeue
from collections import deque

q = deque()

# Enqueue
q.append(10)
q.append(20)
q.append(30)

print("Queue after enqueue:", list(q))

# Dequeue
print("Dequeued:", q.popleft())
print("Queue now:", list(q))