# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.\
# The overall run time complexity should be O(log (m+n)).
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = nums1 + nums2
        mergedArray.sort()
        mergedArraySize = len(mergedArray)
        if mergedArraySize % 2 == 0:
            return (mergedArray[(mergedArraySize // 2) - 1] + mergedArray[(mergedArraySize // 2)]) / 2
        else:
            return mergedArray[(mergedArraySize // 2)]