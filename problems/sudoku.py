from os import system
from typing import List


class Solution:
    solved = False

    def validBlock(self, block: List[str]) -> bool:
        blanks = block.count(".")
        distinctNums = set(filter(lambda x: x != ".", block))

        return len(distinctNums) + blanks == 9

    def getRow(self, board, x) -> List[str]:
        return board[x]

    def getCol(self, board, y) -> List[str]:
        return [board[x][y] for x in range(9)]

    def getSquare(self, board, x, y) -> List[str]:
        row, col = (x // 3, y // 3)
        return [board[x + (row * 3)][y + (col * 3)] for y in range(3) for x in range(3)]

    def validSpace(self, board, x, y) -> bool:
        if not self.validBlock(self.getRow(board, x)):
            return False

        if not self.validBlock(self.getCol(board, y)):
            return False

        if not self.validBlock(self.getSquare(board, x, y)):
            return False

        return True

    def printBoard(self, board) -> None:
        system("clear")
        for x in range(9):
            if x % 3 == 0 and x > 0: print(" ".join(["-"]*11))
            row = board[x]
            split3 = [row[:3], row[3:6], row[6:9]]
            row_print = " | ".join([" ".join(block) for block in split3])
            print(row_print)

    def solver(self, board, possible_solutions: List[tuple]):
        if len(possible_solutions) > 0:
            space, options = possible_solutions[0]
            x, y = space
            for option in options:
                board[x][y] = option
                self.printBoard(board)
                print(f"valid: {self.validSpace(board, x, y)}")
                [print(s) for s in possible_solutions[:5]]
                # input()

                if self.validSpace(board, x, y):
                    if self.solver(board, possible_solutions[1:]):
                        return True
                    else:
                        board[x][y] = "."
                else:
                    board[x][y] = "."
            return False
        else:
            return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numbers = set([str(n) for n in range(1, 10)])
        possible_solutions = []

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    possible_solutions.append(((x, y),
                                               numbers
                                               - set(self.getRow(board, x))
                                               - set(self.getCol(board, y))
                                               - set(self.getSquare(board, x, y))))

        # possible_solutions.sort(key=lambda elem: (len(elem[1]), elem))
        possible_solutions.sort(key=lambda elem: len(elem[1]))
        self.solver(board, possible_solutions)


input_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Solution().solveSudoku(input_board)
