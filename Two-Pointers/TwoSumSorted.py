from typing import List

class Solution:
    def twoSum_sorted(self, nums: List[int], target: int) -> List[int]:
        l_index: int = 0
        r_index: int = len(nums)

        while l_index < r_index:
            curr_sum: int = nums[l_index] + nums[r_index]
            if (curr_sum > target):
                # sum too large, move right index left to smaller number
                r_index -= 1
            elif (curr_sum < target):
                # sum too small, move left index right to larger number
                l_index += 1
            else:
                # nums[l_index] + nums[r_index] = target, return indices
                return [l_index, r_index]
        
        # else return an empty array
        return []
