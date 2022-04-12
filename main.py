from problems.algorithms.problems_to_0100.problem_0018_4Sum import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.fourSum([1,0,-1,0,-2,2], 0)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
