import QuickSort
from typing import List

class Solution:
    def threeSum_toZero(self, nums: List[int]) -> List[List[int]]:
        #initialize returned result
        result = []

        #sort input array
        QuickSort.QuickSort(nums, 0, len(nums)-1)

        for index, value in enumerate(nums):

            # unless dealing with the very first element check to make sure
            # the value being evaulated in current iteration is not a 
            # repeat of a previously evaluated value
            if index > 0 and value == nums[index - 1]:
                continue;

            l_index, r_index = index+1, len(nums)-1
            while (l_index < r_index):
                current_sum = value + nums[l_index] + nums[r_index]
                if (current_sum < 0):
                    # too small, increment left index to larger value 
                    l_index += 1
                elif (current_sum > 0):
                    # too big, decrement right index to smaller value
                    r_index -= 1
                else:
                    # solution found 
                    result.append([value, nums[l_index], nums[r_index]])
                    
                    # skip over duplicate left index values to 
                    # avoid adding duplicates to solution
                    l_index += 1
                    while nums[l_index] == nums[l_index-1] and l_index < r_index:
                        l_index += 1
                        
        return result