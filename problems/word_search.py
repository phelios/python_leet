from typing import List


class Solution:

    def populate_stack(self, x, y, height, width, visited):
        neighbours = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]

        for pos in neighbours:
            next_x = pos[0]
            next_y = pos[1]
            if -1 < next_x < height \
                    and -1 < next_y < width \
                    and (next_x, next_y) not in visited:
                yield next_x, next_y

    def dfs(self, node, visited, board, word, match, height, width):
        x = node[0]
        y = node[1]
        potential_visit = visited + [node]
        potential_match = match + board[x][y]
        if word.startswith(potential_match):
            if potential_match == word:
                return True

            for new_node in self.populate_stack(x, y, height, width, potential_visit):
                if self.dfs(new_node, potential_visit, board, word, potential_match, height, width):
                    return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        for x in range(height):
            for y in range(width):
                node = (x, y)
                visited = []
                match = ""
                if self.dfs(node, visited, board, word, match, height, width):
                    return True
        return False


solution = Solution().exist([["a","a","a","a"],["c","d","s","l"]], "acdb")
print(solution)
