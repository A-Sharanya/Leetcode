class Solution:
    def findComplement(self, num: int) -> int:
        todo = num
        mask = 1
        while todo > 0:
            todo >>= 1
            mask <<= 1
        mask -= 1
        return num ^ mask