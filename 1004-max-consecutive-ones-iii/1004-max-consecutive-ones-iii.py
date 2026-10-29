class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        zerocount = 0
        l = 0

        for r in range(n):
            if nums[r] == 0:
                zerocount+=1
            if (zerocount > k):
                if (nums[l]==0):
                    zerocount-=1
                l+=1
        return len(nums)-l
        