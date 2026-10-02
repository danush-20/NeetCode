class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {}
        res = 0
        l = 0
        for i in range(len(fruits)):
            freq[fruits[i]] = freq.get(fruits[i],0)+1

            while (len(freq) > 2):
                freq[fruits[l]] -= 1
                if(freq[fruits[l]] == 0):
                    del freq[fruits[l]]
                l+=1
            res = max(res,i-l+1)
        return res
        