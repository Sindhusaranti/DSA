class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res=[]
        for i in range(left,right+1):
            num=i
            i=str(i)
            if '0' not in i:
                i=int(i)
                while i!=0:
                    isselfdiv=True
                    rem=i%10
                    if num%rem!=0:
                        isselfdiv=False
                        break
                    i=i//10
                if isselfdiv==True:
                    res.append(num)
        return res
