"""
https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/description/
"""


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        nBin = bin(n)[2:]
        kBin = bin(k)[2:]

        nLen = len(nBin)
        kLen = len(kBin)

        if nLen < kLen:
            return -1

        res = 0

        for i in range(-kLen, 0):
            if nBin[i] == "0" and kBin[i] == "1":
                return -1
            if nBin[i] == "1" and kBin[i] == "0":
                res += 1

        for i in range(nLen - kLen):
            if nBin[i] == "1":
                res += 1

        return res


solution = Solution()
print(solution.minChanges(13, 4))
print(solution.minChanges(21, 21))
print(solution.minChanges(14, 13))
