from problems.algorithms.problem_0069_sqrt import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.mySqrt(16)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
