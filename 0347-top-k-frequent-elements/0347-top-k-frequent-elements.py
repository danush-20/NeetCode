class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] = d.get(i) + 1
        d_sorted = sorted(d,key=d.get,reverse=True)
        return d_sorted[:k]
