from typing import List

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #initialize local variables 
        duplicateFound: bool = False
        current_int: int = 0

        if not nums:
            # list is empty
            duplicateFound = False
        else:
            while nums:
                current_int = nums.pop(0)
                for n in nums:
                    if (current_int == n):
                        # duplicate found
                        duplicateFound = True
                        break
                    
        return duplicateFound

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #initialize local variables
        duplicateFound: bool = False
        duplicateScanMemory: set = set()

        for n in nums:
            if n in duplicateScanMemory:
                duplicateFound = True
                break
            else:
                duplicateScanMemory.add(n)

        return duplicateFound