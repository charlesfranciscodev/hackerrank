from collections import Counter

def ransom_note(magazine, ransom):
    word_counter = Counter(magazine)
    for word in ransom:
        if word_counter[word] == 0:
            return False
        word_counter[word] -= 1
    return True

m, n = map(int, input().strip().split())
magazine = input().strip().split()
ransom = input().strip().split()
print("Yes" if ransom_note(magazine, ransom) else "No")
