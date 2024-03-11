import ContainsDuplicate
import IsAnagram
import TwoSum
import GroupAnagram
import TopK_FrequentElements
import InvertBinaryTree
from InvertBinaryTree import BinaryTreeNode
from InvertBinaryTree import Solution
from InvertBinaryTree import BinaryTree
import ProductofArrayExceptSelf

import random

# source:
# https://neetcode.io/practice

def main():
    Sol1 = ContainsDuplicate.Solution1()
    Sol1_1 = ContainsDuplicate.Solution2()
    print(Sol1.containsDuplicate([1,2,3,4,4]))
    print(Sol1_1.containsDuplicate([1,2,3,4,4]))

    #Sol2 = IsAnagram.SolutionA()
    #print(Sol2.IsAnagram("anagram", "nagaram"))

    #Sol3 = TwoSum.Solution()
    #print(Sol3.twoSum([1,2,3,4], 4))

    #Sol4 = GroupAnagram.Solution()
    #print(Sol4.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

    #Sol5 = TopK_FrequentElements.Solution()
    #print(Sol5.topKFrequent([1,1,1,2,2,3], 2))

    #Sol6 = ProductofArrayExceptSelf.solutionA()
    #print(Sol6.productExceptSelf([1,2,3,4]))

    
    #SolX = InvertBinaryTree.Solution()
    #rand_BTree: BinaryTree = InvertBinaryTree.BinaryTree(None,0,15)
    #print("\n Initial Tree: \n")
    #rand_BTree.printTree()
    #inverted_BTree: BinaryTree | None  = InvertBinaryTree.BinaryTree(SolX.invertBinaryTree(rand_BTree.root))
    #print("\n Inverted Tree: \n")
    #inverted_BTree.printTree()

    #Sol7 is Valid soduko, still need to test

    #Sol8 is locked

    #Sol9 is Longest Consecutive Sequence, still need to test





    
    




if __name__ == "__main__":
    main()