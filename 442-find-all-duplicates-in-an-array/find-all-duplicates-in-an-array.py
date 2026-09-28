class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        res=[]
        for key,value in freq.items():
            if value==2:
                res.append(key)
        return res