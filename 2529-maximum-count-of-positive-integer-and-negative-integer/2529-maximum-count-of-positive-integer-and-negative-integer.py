class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = 0
        p = 0
        for i in nums:
            if i > 0:
                p += 1
            elif i < 0:
                n +=1
        return max(n,p)