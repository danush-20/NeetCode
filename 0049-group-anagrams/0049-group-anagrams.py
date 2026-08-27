class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            t = ''.join(sorted(i))
            d[t]=[]
        
        for i in strs:
            t = ''.join(sorted(i))
            d[t].append(i)

        return list(d.values())

