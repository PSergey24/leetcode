from problems.algorithms.problems_to_0300.problem_0279_perfect_squares import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.numSquares(6)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
