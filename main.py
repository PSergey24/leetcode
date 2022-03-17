from problems.algorithms.problem_0005_longest_palindromic_substring import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.longestPalindrome("babadabab")
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
