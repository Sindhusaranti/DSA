class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        total=1
        for n in range(2,int(num**0.5)+1):
            if num%n==0:
                total+=n
                total+=num//n
        return total==num