class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum=0
        for i in range(len(mat)):
            sum=sum+mat[i][i]
        for i in range(len(mat)):
            sum=sum+mat[i][len(mat)-1-i]
        if len(mat)%2!=0:
            sum=sum-mat[len(mat)//2][len(mat)//2]
        return sum

        