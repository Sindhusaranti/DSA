class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums+=nums
        return nums