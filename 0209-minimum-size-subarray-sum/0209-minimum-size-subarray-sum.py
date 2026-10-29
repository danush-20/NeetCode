class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float('inf')
        l=0
        sumsub=0
        for i in range(len(nums)):
            sumsub+=nums[i]
            while(sumsub>=target):
                res = min(res,i-l+1)
                sumsub-=nums[l]
                l+=1
        if res == float('inf'):
            return 0
        else:
            return res
            