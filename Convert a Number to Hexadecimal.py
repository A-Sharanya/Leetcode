class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_map = "0123456789abcdef"
        
        if num < 0:
            num = (1 << 32) + num
            
        result = []
        while num > 0:
            result.append(hex_map[num & 15])
            num >>= 4
            
        return "".join(reversed(result))