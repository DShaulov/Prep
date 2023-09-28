from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        permutations = self.permuteRecursive([], nums)
        permutationsSet = set()
        permutationsUnique = []
        for i in range(len(permutations)):
            if tuple(permutations[i]) in permutationsSet:
                continue
            permutationsSet.add(tuple(permutations[i]))
            permutationsUnique.append(permutations[i])
        return permutationsUnique
    def permuteRecursive(self, current: List[int], nums: List[int]) -> List[List[int]]:
        permutations = []
        if len(nums) == 0:
            return [current]
        for i in range(len(nums)):
            newNums = nums.copy()
            newCurrent = current.copy()
            newCurrent.append(nums[i])
            newNums.pop(i)
            permutations = permutations + self.permuteRecursive(newCurrent, newNums)
        return permutations

sol = Solution()
print(sol.permuteUnique([1, 1, 2]))