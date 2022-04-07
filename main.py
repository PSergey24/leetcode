from problems.algorithms.problem_0264_ugly_number_II import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.nthUglyNumber(10)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
