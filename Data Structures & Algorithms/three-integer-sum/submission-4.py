class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        start=0
        i=1
        j=len(nums)-1
        ans=[]

        while start<=len(nums)-3:
            while i<j:
                if nums[start]+nums[i]+nums[j]==0 and [nums[start],nums[i],nums[j]] not in ans:
                    ans.append([nums[start],nums[i],nums[j]])
                    if j-i>0:
                        j-=1
                    else: 
                        i+=1
                        j=len(nums)-1 
                elif nums[start]+nums[i]+nums[j]>0: 
                    j-=1
                else:
                    i+=1
            
            start+=1
            i=start+1
            j=len(nums)-1

        return ans

        