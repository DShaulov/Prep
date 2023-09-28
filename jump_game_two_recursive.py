from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.recursiveJump(nums, 0, len(nums))
    def recursiveJump(self, nums: List[int], jumpCount: int, maxJump) -> int:
        if len(nums) == 1:
            return jumpCount
        # Jump to each possible point 
        lowestJumpCount = maxJump
        for i in range(nums[0]):
            if i >= len(nums) - 1:
                continue
            jumps = self.recursiveJump(nums[i+1:], jumpCount + 1, maxJump)
            if jumps < lowestJumpCount:
                lowestJumpCount = jumps
        return lowestJumpCount

sol = Solution()
print(sol.jump([2, 3, 1, 1, 4]))
print(sol.jump([2, 1]))
