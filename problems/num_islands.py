import os
from copy import deepcopy
from typing import List

def print_world(grid, x, y):

    grid_print = deepcopy(grid)
    grid_print[x][y] = "X"

    for y1 in grid_print:
        print(y1)

class NumIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.world_map = {}
        self.n = 0
        self.grid = grid

        height = len(grid)
        width = len(grid[0])

        for y in range(height):
            for x in range(width):
                found_land = self.is_next_to_land(x, y)

                if found_land:
                    self.n += 1

        return self.n

    def is_next_to_land(self, x, y):

        try:
            if self.grid[y][x] == 0:
                return False
        except IndexError:
            return False

        # print_world(self.grid, x, y)

        is_new_land = self.fill_land(x, y)

        if not is_new_land:
            return False

        directions = {
            "above": [x, y-1],
            "right": [x+1, y],
            "below": [x, y+1],
            "left": [x-1, y]
        }

        for direction in directions.values():
            x1 = direction[0]
            y1 = direction[1]

            self.is_next_to_land(x1, y1)

        return True

    def fill_land(self, x, y):
        try:
            if x < 0 \
                or y < 0 \
                or self.world_map[x][y]:
                    return False
        except KeyError:
            pass

        if x not in self.world_map:
            self.world_map[y] = {}

        self.world_map[x][y] = self.n

        return True