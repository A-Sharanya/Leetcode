from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        for char in t:
            if count_s[char] == 0:
                return char
            count_s[char] -= 1