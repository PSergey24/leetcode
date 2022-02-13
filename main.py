from problems.algorithms.problem_0039_combination_sum import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.combinationSum([2], 1)
        print(answer)



if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
