class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for i in nums:
            if i in numsSet:
                return True
            else:
                numsSet.add(i)
        return False