class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        combinedWord = []

        while l < len(word1) and r < len(word2):
            combinedWord.append(word1[l])
            combinedWord.append(word2[r])
            l += 1
            r += 1
        
        if l < len(word1):
            combinedWord.append(word1[l:])
        else:
            combinedWord.append(word2[r:])
        
        return "".join(combinedWord)