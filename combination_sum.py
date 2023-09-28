from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == [] or sum(candidates) < target:
            return []
    def combinationSumRecursive(self, candidates: List[int], current: List[int], target: int) -> List[List[int]]:
        currentSum = sum(current)
        if currentSum == target:
            return [current]
        if currentSum > target:
            return []
        