class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq={}
        for x in arr:
            freq[x]=freq.get(x,0)+1
        occurance=set()
        for value in freq.values():
            if value in occurance:
                return False
            occurance.add(value)
        return True