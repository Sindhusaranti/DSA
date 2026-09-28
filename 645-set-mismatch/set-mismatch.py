class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
            res=[0]*2
        for key,value in freq.items():
            if value==2:
                res[0]=key
        for i in range(1,len(nums)+1):
            if i not in freq:
                res[1]=i  
        return res
