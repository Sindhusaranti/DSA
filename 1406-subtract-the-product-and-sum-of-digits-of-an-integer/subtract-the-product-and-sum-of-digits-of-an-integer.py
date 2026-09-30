class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total=0
        pro=1
        while n!=0:
            total=total+(n%10)
            pro=pro*(n%10)
            n=n//10
        return pro-total
