from problems.algorithms.problems_to_0200.problem_0119_pascals_triangle_II import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.getRow(3)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
