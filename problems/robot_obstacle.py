class RobotObstacle:
    def solve(self, grid):
        self.height = len(grid)
        self.width = len(grid[0])

        self.grid = grid
        self.steps = 0
        self.queue = []

        self.queue.append([0, 0])

        while self.queue:
            node = self.queue.pop(0)
            self.steps += 1
            x = node[0]
            y = node[1]
            self.grid[x][y] = 0

            directions = [
                [x, y-1],
                [x, y+1],
                [x-1, y],
                [x+1, y]
            ]

            for direction in directions:
                x1 = direction[0]
                y1 = direction[1]

                is_valid = self.valid(x1, y1)
                if is_valid == False:
                    return self.steps
                elif is_valid == True:
                    self.queue.append([x1, y1])


    def valid(self, x, y):
        if 0 <= x < self.height and 0 <= y < self.width:
            if self.grid[x][y] == 1:
                return True
            elif self.grid[x][y] == 9:
                return False

        return None
