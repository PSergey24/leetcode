from problems.algorithms.problem_0078_subsets import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.subsets([1,2,3])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
