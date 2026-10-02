class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        for x in nums:
            if x%3!=0:
                res+=1
        return res 
