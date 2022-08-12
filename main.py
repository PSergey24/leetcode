from problems.algorithms.problems_to_0100.problem_0041_first_missing_positive import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.firstMissingPositive([3,0,6,3])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
