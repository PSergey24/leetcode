from problems.algorithms.problem_0014_longest_common_prefix import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.longestCommonPrefix(["fl","flow","f"])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
