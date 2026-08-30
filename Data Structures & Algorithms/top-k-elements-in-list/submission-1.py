class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]=d.get(i)+1

        l=[]
        for i in range(k):
            v = self.max(d)
            l.append(v)
            del d[v]
        return l

        
    def max(self,d):
        value,key=0,0
        for i,j in d.items():
            if value < j:
                value=j
                key=i
        return key
        