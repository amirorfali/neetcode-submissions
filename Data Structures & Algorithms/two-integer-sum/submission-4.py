class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen=set()

      for i in range(len(nums)):
        remain=target-nums[i]
        if remain in seen:
            return [nums.index(remain), i]
        else:
            seen.add(nums[i])

