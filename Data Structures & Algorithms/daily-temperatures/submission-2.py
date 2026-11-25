class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []                                    # holds INDICES of waiting days

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()                       # day j finally found a warmer day
                ans[j] = i - j
            stack.append(i)

        return ans