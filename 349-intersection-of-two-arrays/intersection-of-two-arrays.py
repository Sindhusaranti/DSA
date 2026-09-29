class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq1={}
        freq2={}
        res=[]
        for x in nums1:
            freq1[x]=freq1.get(x,0)+1
        for x in nums2:
            freq2[x]=freq2.get(x,0)+1
        for x in freq1:
            if x in freq2:
                res.append(x)
        return res
