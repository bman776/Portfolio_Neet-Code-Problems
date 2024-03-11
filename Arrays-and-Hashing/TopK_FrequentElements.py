from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result: List[int] = []
        element_counts: dict = {}
        
        element_frequency = [[] for i in range(len(nums)+1)]
        # element_frequency is 2D array where each index contains 
        # a sub array containing all the element from input array that occur
        # with frequency equal to that index

        for n in nums:
            element_counts[n] = 1 + element_counts.get(n, 0)

        for n, c in element_counts.items():
            element_frequency[c].append(n)

        while len(result) < k:
            result = result + element_frequency.pop(-1)

        result = result[-k:]

        return result
