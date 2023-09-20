from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestDist = 0
        closestVal = 0
        first = True
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    dist = abs(target - sum)
                    if first or dist < closestDist:
                        closestDist = dist
                        closestVal = sum
                        first = False
        return closestVal

sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))
print(sol.threeSumClosest([0,0,0], 1))


""" 
Edge Cases:
    Very large numbers - not a problem
    Distance exactly 0
    Iterating out of bounds
    Negative distance - solved with abs
    Repeating triplets - solved in range(i+1, ...)
    Time limit
 """