from problems.algorithms.problem_0020_valid_parenntheses import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.isValid("(()[]{[]}")
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
