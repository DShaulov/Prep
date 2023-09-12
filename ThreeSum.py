from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletDict = {}      
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # Create a copy of the number list and remove the first occurences of the two numbers
                poppedList = [x for x in nums]
                poppedList.remove(nums[i])
                poppedList.remove(nums[j])
                if - (nums[i] + nums[j]) in poppedList:
                    tripletTuple = tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])]))
                    tripletDict[tripletTuple] = tripletTuple
        tripletList = []
        for value in tripletDict.values():
            tripletList.append(list(value))
        return tripletList


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))

# tripletDict = {}      
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 # Create a copy of the number list and remove the first occurences of the two numbers
#                 poppedList = [x for x in nums]
#                 poppedList.remove(nums[i])
#                 poppedList.remove(nums[j])
#                 if - (nums[i] + nums[j]) in poppedList:
#                     tripletTuple = tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])]))
#                     tripletDict[tripletTuple] = tripletTuple
#         tripletList = []
#         for value in tripletDict.values():
#             tripletList.append(list(value))
#         return tripletList