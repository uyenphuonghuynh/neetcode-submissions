class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sqrs = set()
        rows = set()
        cols = set()
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                if (r, board[r][c]) in rows or (c, board[r][c]) in cols:
                    return False
                else:
                    cols.add((c, board[r][c]))
                    rows.add((r, board[r][c]))
                
                if (r//3,c//3, board[r][c]) in sqrs:
                    return False
                else:
                    sqrs.add((r//3,c//3, board[r][c]))
        return True
                    
                

