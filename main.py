from problems.algorithms.problem_0022_generate_parentheses import Solution
from problems.algorithms.problem_0392_is_subsequence import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.isSubsequence("ahbdc", "ahbgdc")
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
