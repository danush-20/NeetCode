from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        n = len(nums)
        res = []
        for i in range(len(nums)):
            while(q and nums[q[-1]] < nums[i]):
                q.pop()
            while(q and q[0] <= i-k):
                q.popleft()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
        return res

        