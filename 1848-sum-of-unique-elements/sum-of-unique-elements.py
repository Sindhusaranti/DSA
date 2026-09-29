class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq={}
        sum=0
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for key,value in freq.items():
            if value==1:
                sum=sum+key
        return sum

        