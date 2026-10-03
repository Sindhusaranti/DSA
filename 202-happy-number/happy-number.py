class Solution:
    def isHappy(self, n: int) -> bool:
        def sqsum(num):
            total=0
            while num>0:
                rem=num%10
                total+=rem*rem
                num//=10
            return total
        slow=n
        fast=sqsum(n)
        while slow!=fast and fast!=1:
            slow=sqsum(slow)
            fast=sqsum(sqsum(fast))
        return fast==1
            