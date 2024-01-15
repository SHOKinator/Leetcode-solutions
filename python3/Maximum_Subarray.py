class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            curNums = 0
            for j in range(i, len(nums)):
                curNums += nums[j]
                ans = max(ans, curNums)
        return ans