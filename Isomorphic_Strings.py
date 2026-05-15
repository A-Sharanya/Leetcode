class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in map_s:
                if map_s[char_s] != char_t:
                    return False
            else:
                map_s[char_s] = char_t
                
            if char_t in map_t:
                if map_t[char_t] != char_s:
                    return False
            else:
                map_t[char_t] = char_s
                
        return True