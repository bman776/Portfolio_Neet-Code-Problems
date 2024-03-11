from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        leftPointer, rightPointer = 0, (len(height)-1)

        while leftPointer < rightPointer:
            curr_area = (rightPointer - leftPointer) * min(height[leftPointer], height[rightPointer])
            if (curr_area > maxArea):
                maxArea = curr_area

            if (height[leftPointer] < height[rightPointer]):
                leftPointer += 1
            elif (height[leftPointer] > height[rightPointer]):
                rightPointer -= 1
            else:
                rightPointer -= 1

        return maxArea