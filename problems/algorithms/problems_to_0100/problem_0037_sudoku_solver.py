from typing import List


class Solution:
    # time complexity O((9!)^9)
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])

                    rows[i].add(num)
                    cols[j].add(num)

                    box_id = i // 3 * 3 + j // 3
                    boxes[box_id].add(num)
                    
        def backTrack(i, j):
            nonlocal isSolved

            if i == 9:
                isSolved = True
                return

            new_i = i + (j + 1) // 9
            new_j = (j+1) % 9

            if board[i][j] != '.':
                backTrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    box_id = i // 3 * 3 + j // 3
                    if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[box_id].add(num)
                        board[i][j] = str(num)
                        backTrack(new_i, new_j)

                        if isSolved is True:
                            break

                        rows[i].remove(num)
                        cols[j].remove(num)
                        boxes[box_id].remove(num)
                        board[i][j] = '.'

        isSolved = False
        backTrack(0, 0)
        print(board)
