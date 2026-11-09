class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]

        seen=dict()

        for num in nums:
            seen[num]=seen.get(num,0)+1
        
        bucket=[[] for _ in range(len(nums)+1)]
        
        for key,value in seen.items():
            bucket[value].append(key)

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans



