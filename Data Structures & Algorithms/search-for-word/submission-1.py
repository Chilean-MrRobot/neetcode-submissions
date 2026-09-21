class Solution:
    def do_dfs_pos(self, i, j, word, pos, board):
        checked_cells.append((i,j))
        cell = board[i][j]
 #       print(f"Func {i},{j},{pos},{word},{word[pos]},{cell},{checked_cells}")
        if cell == word[pos]:
            if pos == len(word) - 1:
                return True
            else:
                if i > 0 and (i-1,j) not in checked_cells:
                    word_completed = self.do_dfs_pos(i-1, j, word, pos+1, board)
                    if word_completed:
                        return True
                if i + 1 < len(board) and (i+1,j) not in checked_cells:
                    word_completed = self.do_dfs_pos(i+1, j, word, pos+1, board)
                    if word_completed:
                        return True
                if j > 0 and (i,j-1) not in checked_cells:
                    word_completed = self.do_dfs_pos(i, j-1, word, pos+1, board)
                    if word_completed:
                        return True
                if j + 1 < len(board[0]) and (i,j+1) not in checked_cells:
                    word_completed = self.do_dfs_pos(i, j+1, word, pos+1, board)
                    if word_completed:
                        return True
        checked_cells.pop()
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        global checked_cells
        word_completed = False
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                checked_cells = []
                pos = 0
#                print(f"{i} {j} {board[i][j]} {checked_cells}")
                word_completed = self.do_dfs_pos(i, j, word, pos, board)
                if word_completed:
                    return True
        return False
        