from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counts = Counter(magazine)
        note_counts = Counter(ransomNote)
        for char, count in note_counts.items():
            if mag_counts[char] < count:
                return False
        return True