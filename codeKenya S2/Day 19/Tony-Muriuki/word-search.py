from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            # If we matched all characters in word
            if i == len(word):
                return True
            
            # Out of bounds or mismatch
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            # Mark this cell as visited
            temp, board[r][c] = board[r][c], "#"

            # Explore all 4 directions
            found = (
                backtrack(r+1, c, i+1) or
                backtrack(r-1, c, i+1) or
                backtrack(r, c+1, i+1) or
                backtrack(r, c-1, i+1)
            )

            # Restore the cell (backtrack)
            board[r][c] = temp

            return found

        # Try starting from every cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False
