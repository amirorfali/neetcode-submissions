class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:          # num starts a sequence
                length = 1
                while num + length in numSet:  # walk up: num+1, num+2, ...
                    length += 1
                longest = max(longest, length)

        return longest