from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result: List[int] = [-1 for i in range(2)]

        # scan input array nums
        array_scan_ValPos_Memory: dict = {}
        for index, num in enumerate(nums):
            
            if array_scan_ValPos_Memory.get(target - num) is None:
                array_scan_ValPos_Memory[num] = index
            else:
                result[0] = index
                result[1] = array_scan_ValPos_Memory[num-target]

        
        return result