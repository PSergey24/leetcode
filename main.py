from problems.algorithms.problems_to_0200.problem_0200_number_of_islands import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        answer = solution.numIslands(grid)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
