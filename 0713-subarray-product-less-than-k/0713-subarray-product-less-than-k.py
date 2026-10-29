class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if (k<=1):
            return 0
        l = 0 
        prod = 1
        res = 0
        for i in range(len(nums)):
            prod *= nums[i]
            while (prod >= k):
                prod //= nums[l]
                l+=1
            res += i-l+1
        return res

        