class Solution:
    def countDigits(self, num: int) -> int:
        res=0
        n=num
        while num!=0:
            rem=num%10
            if n%rem==0:
                res+=1
            num=num//10
        return res
        