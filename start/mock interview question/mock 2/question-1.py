'''
Q1. Easy – Reverse Words in a Sentence
'''

def reverse_words(sentence:str) -> str:
    return " ".join(sentence.split()[::-1])

print(reverse_words("I love Python"))