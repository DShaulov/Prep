from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head = 0
        right = 1
        while (right < len(nums)):
            if (nums[head] == nums[right]):
                nums[right] = 1000
                right += 1
            else:
                head = right
                right += 1
        nums.sort()
        try:
            return nums.index(1000)
        except ValueError:
            return len(nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))