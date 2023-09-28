from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        queue = [0]
        indicesAdded = set()
        for jumps in range(len(nums)):
            nextQueue = []
            for index in queue:
                if index == target:
                    return jumps
                for j in range(nums[index]):
                    if j+index <= target:
                        if (index + j + 1) not in indicesAdded:
                            nextQueue.append(index+j+1)
                            indicesAdded.add(index+j+1)
            queue = nextQueue


sol = Solution()
print(sol.jump([2, 3, 1, 1, 4]))
print(sol.jump([2, 1]))
