class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for key,value in freq.items():
            if value!=1:
                return key