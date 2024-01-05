class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stopLoop = False
        ansList =[]
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i < j and nums[i] + nums[j] == target:
                    ansList.append(i)
                    ansList.append(j)
                    stopLoop = True
                    break
            if stopLoop:
                break

        return ansList
