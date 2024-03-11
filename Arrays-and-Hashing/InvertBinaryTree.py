import random

class BinaryTreeNode:
    def __init__(self, val:int=0, left_child=None, right_child=None):
        self.val = val
        self.right_child = right_child
        self.left_child = left_child


class BinaryTree:
    ''' 
    constructor for RandomBinaryTree 
    seed: the seed value for the random number generator used to generate random node values
    num_of_nodes: the number of nodes to constrnct the tree with (must be greater than or equal to 1)
    depth: the level to which the tree will be built (must be non-negative, root is defined to be @ depth lvl 0)
    ''' 
    def __init__(self, root:BinaryTreeNode|None=None, seed:int|None=None, num_of_nodes:int|None=None):

        # define attributes
        self.root: BinaryTreeNode | None = None
        self.num_of_nodes: int | None = None
        self.seed: int | None = None

        if (root is not None):
            # an exisiting binary tree node has been supplied as the root of the binary tree
            self.root = root
        elif (seed is not None and num_of_nodes is not None):
            # a random number generator seed and number of nodes to generate has been provided

            # check + initialize number of nodes
            # number of nodes must be greater than or equal to 1
            if (num_of_nodes < 1):
                print("Please enter a positive integer for the number of nodes of binary tree")
                return
            self.num_of_nodes = num_of_nodes
            # seed random number generator
            random.seed(seed)
            self.root = self.__buildTree(self.num_of_nodes)
        else:
            self.root = None 

    '''
    Builds the Binary Tree
    '''
    def __buildTree(self, node_num) -> BinaryTreeNode | None:

        # initialize local variables
        node: BinaryTreeNode | None = None
        rem_nodes: int = -1
        left_rem_nodes: int = -1
        right_rem_nodes: int = -1

        if (node_num <= 0):
            # number of nodes is negative or 0 
            # tree construction complete, begin returning
            return None
        # else number of nodes is >= 1, randomly build a genuine binary tree

        # build node of Binary Tree
        node = BinaryTreeNode(random.randint(0,100))
        rem_nodes = node_num - 1

        if (rem_nodes > 0):
            # split number of remaining nodes between left and right branches
            # build left and right branches
            left_rem_nodes = rem_nodes // 2 + (rem_nodes % 2)
            node.left_child = self.__buildTree(left_rem_nodes)
            right_rem_nodes = rem_nodes // 2
            node.right_child = self.__buildTree(right_rem_nodes)

        # tree construction complete, begin returning
        return node
    
    def printTree(self, node:BinaryTreeNode | None = None, spacer:str = "\t", prefix:str = "") -> None:
        if (node is None):
            node = self.root
        assert node is not None
        
        if (node.right_child != None):
            self.printTree(node.right_child, spacer + spacer[0], "/")
        
        print(spacer + prefix + str(node.val) + "--|")

        if (node.left_child != None):
            self.printTree(node.left_child, spacer + spacer[0], "\\")
        
        
class Solution:
    def invertBinaryTree(self, root: BinaryTreeNode | None) -> BinaryTreeNode | None:

        if (root is None):
            return None
        assert root is not None

        if (root.left_child != None and root.right_child != None):
            # root has both children, perform inversion

            # save roots left child
            root_LchildTemp = root.left_child
            # swap roots children
            root.left_child = root.right_child
            root.right_child = root_LchildTemp

            self.invertBinaryTree(root.left_child)
            self.invertBinaryTree(root.right_child)
        
        return root 