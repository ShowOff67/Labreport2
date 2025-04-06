class IterativeDeepeningSearch:
    def __init__(self):
        self.found = False

    def start_search(self, grid, goal):
        rows = len(grid)
        cols = len(grid[0])

        depth = 1
        while not self.found:
            self.path = []
            self.found = False
            visited = [[False] * cols for _ in range(rows)]
            self.dfs(grid, 0, 0, goal, depth, visited)

            if self.found:
                print("Path found:", self.path)
                break

            depth += 1

    def dfs(self, grid, row, col, goal, depth, visited):
        if (row, col) == goal:
            self.path.append((row, col))
            self.found = True
            return

        if depth == 0:
            return

        visited[row][col] = True
        self.path.append((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 0 and not visited[new_row][new_col]:
                self.dfs(grid, new_row, new_col, goal, depth - 1, visited)

                if self.found:
                    return

        self.path.pop()

if __name__ == "__main__":
    try:
        print("Enter the number of rows in the grid:")
        rows = int(input().strip())
        print("Enter the number of columns in the grid:")
        cols = int(input().strip())

        grid = []
        print("Enter the grid (0 for open path, 1 for obstacle):")
        for i in range(rows):
            row = list(map(int, input().strip().split()))
            grid.append(row)

        print("Enter the goal position (row and column):")
        goal_row, goal_col = map(int, input().strip().split())
        goal = (goal_row, goal_col)

        ids = IterativeDeepeningSearch()
        ids.start_search(grid, goal)

    except ValueError:
        print("Invalid input format. Please enter numbers only.")
