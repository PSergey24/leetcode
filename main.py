from problems.algorithms.problem_3_longest_substring_without_repeating_characters import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()
        answer = solution.lengthOfLongestSubstring("a")
        print(answer)

if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
