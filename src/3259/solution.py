from typing import List

"""
https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/
"""


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        maxA = energyDrinkA[0]
        maxB = energyDrinkB[0]
        for i in range(1, len(energyDrinkA)):
            tempMaxA = max(maxA + energyDrinkA[i], maxB)
            tempMaxB = max(maxB + energyDrinkB[i], maxA)
            maxA = tempMaxA
            maxB = tempMaxB
        return max(maxA, maxB)


solution = Solution()
print(solution.maxEnergyBoost([4, 1, 1], [1, 1, 3]))
