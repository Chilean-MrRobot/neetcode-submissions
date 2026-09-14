class Solution:
    def do_dfs(self, i, j, grid, rows, columns, visited_lands):
        if (i,j) not in visited_lands:
            visited_lands.add((i,j))
        if i > 0:
            if grid[i-1][j] == "1":
                if (i-1,j) not in visited_lands:
                    visited_lands = self.do_dfs(i-1, j, grid, rows, columns, visited_lands)
        if i < rows-1:
            if grid[i+1][j] == "1":
                if (i+1,j) not in visited_lands:
                    visited_lands = self.do_dfs(i+1, j, grid, rows, columns, visited_lands)
        if j > 0:
            if grid[i][j-1] == "1":
                if (i,j-1) not in visited_lands:
                    visited_lands = self.do_dfs(i, j-1, grid, rows, columns, visited_lands)
        if j < columns-1:
            if grid[i][j+1] == "1":
                if (i,j+1) not in visited_lands:
                    visited_lands = self.do_dfs(i, j+1, grid, rows, columns, visited_lands)
        return visited_lands
    
    def numIslands(self, grid: List[List[str]]) -> int:
        counter_islands = 0
        rows, columns = len(grid), len(grid[0])
        visited_lands = set()

        for i, row in enumerate(grid):
            for j, value in enumerate(row):
#                print(i,j,visited_lands)
                if (i,j) in visited_lands:
                    continue
                elif value == "0":
                    visited_lands.add((i,j))
                    continue
                else:
                    counter_islands += 1
                    visited_lands = self.do_dfs(i, j, grid, rows, columns, visited_lands)

        return counter_islands
        