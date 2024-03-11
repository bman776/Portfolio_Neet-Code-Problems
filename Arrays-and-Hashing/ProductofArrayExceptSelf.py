from typing import List
from functools import reduce

class solutionA:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix:int = 1
        suffix:int = 1

        result = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i] 
        
        return result     

class solutionB:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # declare local varaibles
        prefix_product_dict: dict = {}
        suffix_product_dict: dict = {}
        result: dict = {}
        
        prefix_product: int
        suffix_product: int
        for i in range(len(nums)):
            if i == 0:
                prefix_product = 1
                suffix_product = reduce((lambda x, y: x*y), nums[1:])
            elif i == (len(nums)-1):
                prefix_product = reduce((lambda x, y: x*y), nums[:-1])
                suffix_product = 1
            else:
                prefix_product = reduce((lambda x, y: x*y), nums[:i])
                suffix_product = reduce((lambda x, y: x*y), nums[i+1:])
            
            prefix_product_dict[i] = prefix_product
            suffix_product_dict[i] = suffix_product
            result[i] = prefix_product * suffix_product
        
        return list(result.values())

        

        
