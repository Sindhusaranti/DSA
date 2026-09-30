class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        isdiv=0
        isnotdiv=0
        for i in range(1,n+1):
            if i%m==0:
                isdiv=isdiv+i
            else:
                isnotdiv+=i
        return isnotdiv-isdiv