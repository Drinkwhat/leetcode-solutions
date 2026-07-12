class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        res = str(x)
        l = len(res) - 1
        for i in range(len(res) // 2):
            if res[i] != res[l - i]: return False

        return True