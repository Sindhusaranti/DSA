class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq={}
        while n!=0:
            rem=n%10
            freq[rem]=freq.get(rem,0)+1
            n=n//10
        res=0
        for key,value in freq.items():
            res=res+(key*value)
        return res