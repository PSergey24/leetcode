from problems.algorithms.problem_0022_generate_parentheses import Solution
from problems.algorithms.problem_0047_permutations_II import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.permuteUnique([1, 1, 2])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
