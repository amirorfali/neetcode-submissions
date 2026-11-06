class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       numSet=set()
       for i in range(len(nums)):
        remain=target-nums[i]
        if remain in numSet and nums.index(remain)!=i:
            return[nums.index(remain),i]
        else: numSet.add(nums[i])
