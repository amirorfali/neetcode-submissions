class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        start=0
        i=1
        j=len(nums)-1

        while start<=len(nums)-3:
            #if nums[i-1]==nums[i]:
             #   start+=1
              #  i=start+1
            
            while i<j:
                if nums[start]+nums[i]+nums[j]==0 and [nums[start], nums[i], nums[j]] not in ans:
                    ans.append([nums[start], nums[i], nums[j]])
                    j-=1
                elif nums[start]+nums[i]+nums[j]>=0:
                    j-=1
                else: i+=1

            start+=1
            i=start+1
            j=len(nums)-1
        
        return list(ans)
            