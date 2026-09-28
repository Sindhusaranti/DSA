class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=[0]*26
        resindex=0
        unique=False
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')]+=1
        for i in range(len(s)):
            if freq[ord(s[i])-ord('a')]==1:
                resindex=i
                unique=True
                break
        if unique==False:
            return -1
        else:
            return resindex

          