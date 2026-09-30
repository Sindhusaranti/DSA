class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total=0
        for x in nums:
            total=total+x
        return total%k
        