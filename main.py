from problems.algorithms.problem_13_roman_to_integer import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()
        solution.romanToInt(s="MCMXCIV")


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
