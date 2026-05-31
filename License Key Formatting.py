class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        result = []
        n = len(s)
        
        first_group_len = n % k
        if first_group_len > 0:
            result.append(s[:first_group_len])
            
        for i in range(first_group_len, n, k):
            result.append(s[i:i+k])
            
        return "-".join(result)