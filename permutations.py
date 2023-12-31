from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        return self.permuteRecursive([], nums)
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
print(sol.permute([1, 2, 3]))