class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        while p1 >= 0 or p2 >= 0 or carry:
            d1 = int(num1[p1]) if p1 >= 0 else 0
            d2 = int(num2[p2]) if p2 >= 0 else 0
            
            total = d1 + d2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            p1 -= 1
            p2 -= 1
            
        return "".join(reversed(res))