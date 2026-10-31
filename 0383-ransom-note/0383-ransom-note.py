class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in magazine:
            d.update({i:d.get(i,0)+1})
        
        for j in ransomNote:
            if j not in d or d[j] == 0:
                return False
            d[j] -= 1
        return True