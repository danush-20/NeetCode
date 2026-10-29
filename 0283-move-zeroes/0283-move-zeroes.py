class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l , r = 0 , 0 
        while r < len(nums):
            if nums[r] != 0:
                nums[l] , nums[r] = nums[r] , nums[l]
                r+=1
                l+=1
            else:
                r+=1
        
        