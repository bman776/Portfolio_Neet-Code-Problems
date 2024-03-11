class SolutionA:
    def IsAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False
        # else count characters in each string

        s_charCount:dict = {}
        t_charCount:dict = {}
        for character in s:
            s_charCount[character] = s_charCount.get(character, 0) + 1
        for character in t:
            t_charCount[character] = t_charCount.get(character, 0) + 1

        # compare character counts to determine if strings are anagrams
        for (key, val) in s_charCount.items():
            if (t_charCount.get(key) != val):
                return False
        
        return True
    
class SolutionB:
    # https://www.geeksforgeeks.org/python-ways-to-sort-letters-of-string-alphabetically/

    def IsAnagram(self, s: str, t: str) -> bool:
        
        # TODO
        # Solution B involves sorting the input strings using an efficient O(nlgn) sorting algorithm and then directly comparing their sorted forms

        return False

'''My Original Solution'''
class SolutionC:
    def IsAnagram(self, s: str, t: str) -> bool:
        
        # initialize
        is_anagram: bool = False
        s_chars: list[str] = list(s)
        t_chars: list[str] = list(t)
        s_sum: int = 0
        t_sum: int = 0

        while s_chars and t_chars:
            # summarize character contents of input strings as integer sums 
            s_sum += ord(s_chars.pop(0))
            t_sum += ord(t_chars.pop(0))

        if (s_chars and not t_chars) or (not s_chars and t_chars):
            # input string s and t not of same length 
            is_anagram = False
        elif s_sum == t_sum:
            # input string s and t are same length and contain the same characters
            # s and t are anagrams of each other
            is_anagram = True
        else:
            # input strings s and t are the same length but do not contain the same chars
            is_anagram = False
            
        return is_anagram