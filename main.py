from problems.algorithms.problems_to_0100.problem_0036_valid_sudoku import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        answer = solution.isValidSudoku(board)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
