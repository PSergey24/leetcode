from problems.algorithms.problems_to_0100.problem_0056_merge_intervals import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.merge([[1,3],[15,18],[2,6],[8,10]])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
