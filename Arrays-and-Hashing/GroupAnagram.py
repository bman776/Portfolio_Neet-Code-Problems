from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: List[List[str]]

        # DEV NOTE: 
        # a defaultdict is the same as a normal python dictionary only it will never raise a key error and will instead return
        # a default value given to the constructor (in this case an empty list object)
        grouping_dict = defaultdict(list)
        
        for string in strs:
            # DEV NOTE: 
            # lists cannot serve as keys in python dictionaries since they are mutable, and sorted() returns a list
            # so we take the list returned and create an immutable tuple that CAN serve as a key
            grouping_dict[tuple(sorted(string))].append(string)
        
        result = grouping_dict.values() # type: ignore

        return result