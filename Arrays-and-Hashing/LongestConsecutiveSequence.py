from typing import List

class Solution:
    def longestConsecutiveSequence(self, nums: List[int]) -> int:
        numSet: set = set(nums)

        longestConsecutiveSequenceLength: int = 0

        for num in nums:
            if ((num)-1 not in numSet):
                # num is the start of a sequence
                seqLen = 1

                nextNum:int = num + 1
                while ((nextNum) in numSet):
                    seqLen += 1
                    nextNum += 1
                    
                if (seqLen > longestConsecutiveSequenceLength):
                    longestConsecutiveSequenceLength = seqLen
        
        return longestConsecutiveSequenceLength