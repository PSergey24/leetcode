from problems.algorithms.problem_0022_generate_parentheses import Solution
from problems.algorithms.problem_0046_permutations import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.permute([1, 2, 3])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
