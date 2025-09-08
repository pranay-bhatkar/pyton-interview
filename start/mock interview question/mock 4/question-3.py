'''
Q3. Hard – Word Ladder (BFS)
'''

from collections import deque

def ladder_length(beginWord, endWord,wordList):
    wordSet = set(wordList)
    if endWord not in wordSet: return 0
    
    q = deque([(beginWord , 1)])
    while q:
        word, steps = q.popleft()
        if word == endWord: return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new = word[:i] + c + word[i+1:]
                if new in wordSet:
                    wordSet.remove(new)
                    q.append((new, steps+1))
    return 0

print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  
# 5 ("hit" → "hot" → "dot" → "dog" → "cog")