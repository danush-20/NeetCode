class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        val = 0

        p=1
        for i in range(len(nums)):
            res[i] = p
            p*=nums[i]
        
        s=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=s
            s*=nums[j]

        return res


