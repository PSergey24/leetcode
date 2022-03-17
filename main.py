from problems.algorithms.problem_0066_plus_one import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.plusOne([9,9,9])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
