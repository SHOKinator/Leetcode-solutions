class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        numsSet = list(set(nums))

        for i in range(len(numsSet)):
            count = 0
            for j in range(len(nums)):
                if numsSet[i] == nums[j]:
                    count += 1
                if count > len(nums) / 2:
                    return numsSet[i]
