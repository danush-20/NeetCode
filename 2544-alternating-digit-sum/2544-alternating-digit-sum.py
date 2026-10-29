class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        digit=str(n)
        for i in range(1,len(digit)+1):
            if i%2==0:
                res-=int(digit[i-1])
            else:
                res+=int(digit[i-1])
        return res
        