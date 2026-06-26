def anagrams(word1, word2):
    w1=sorted(word1)
    w2=sorted(word2)
    if w1 == w2:
        return "are anagrams"
    return "are not anagrams"

print(f"listen and silent {anagrams('listen', 'silent')}")
print(f"write and books {anagrams('write', 'books')}")
print(f"stop and post {anagrams('stop', 'post')}")