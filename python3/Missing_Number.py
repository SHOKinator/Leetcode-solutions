class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()

        for n in nums:
            if ans == n:
                ans += 1
            else:
                return ans
        return ans
