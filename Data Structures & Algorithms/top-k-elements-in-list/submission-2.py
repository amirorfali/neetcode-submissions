class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[0]*k

        seen=dict()

        for num in nums:
            seen[num]=seen.get(num,0)+1
        

        i=0
        highNum=0
        highKey=0
        while i < len(ans):
            for key, value in seen.items():
            
                if value>highNum:
                    highNum=value
                    highKey=key
            ans[i]=highKey               
            seen.pop(highKey)
            i+=1
            highNum=0
            highKey=0
        
        return ans


