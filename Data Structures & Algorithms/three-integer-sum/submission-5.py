class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        start=0
        i=1
        j=len(nums)-1
        ans=[]

        while start<=len(nums)-3:
            if start>0 and nums[start]==nums[start-1]:   
                start+=1                                 
                i=start+1                                
                j=len(nums)-1                            
                continue     
            while i<j:
                if nums[start]+nums[i]+nums[j]==0:
                    ans.append([nums[start],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                elif nums[start]+nums[i]+nums[j]>0: 
                    j-=1
                else:
                    i+=1
            
            start+=1
            i=start+1
            j=len(nums)-1

        return ans

        