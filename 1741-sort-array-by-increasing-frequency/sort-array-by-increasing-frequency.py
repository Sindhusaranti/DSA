class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq={}
        res=[]
        for x in nums:
            freq[x]=freq.get(x,0)+1
        sorted_freq=dict(sorted(freq.items(),key=lambda x:(x[1],-x[0])))
        for key,value in sorted_freq.items():
                for i in range(value):
                    res.append(key)
        return res