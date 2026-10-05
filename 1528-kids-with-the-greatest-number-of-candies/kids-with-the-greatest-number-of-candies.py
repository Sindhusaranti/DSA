class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        resarr=[]
        for x in candies:
            x+=extraCandies
            res=True
            for y in candies:
                if x<y:
                    res=False
            resarr.append(res)
        return resarr
