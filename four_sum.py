from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                while(left != right and left + 1 != right):
                    numSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if numSum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    elif numSum < target:
                        left += 1
                    else:
                        right += 1
        return quadruplets
    
sol = Solution()
sol.fourSum([1,0,-1,0,-2,2], 0)
sol.fourSum([2,2,2,2,2], 8)
