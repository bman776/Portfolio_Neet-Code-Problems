from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict: dict = defaultdict(set)
        col_dict: dict = defaultdict(set)
        subGrid_dict: dict = defaultdict(set)

        for row_index, row in enumerate(board):
            for row_col_index, row_col_val in enumerate(row):
                if row_col_val == ".":
                    continue
                if (row_col_val in row_dict[row_index] or
                    row_col_val in col_dict[row_col_index] or 
                    row_col_val in subGrid_dict[(row_index//3,row_col_index//3)]):
                    return False
                row_dict[row_index].add(row_col_val)
                col_dict[row_col_index].add(row_col_val)
                subGrid_dict[(row_index//3,row_col_index//3)].add(row_col_val)
        
        return True
                
