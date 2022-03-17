from problems.algorithms.problem_0017_letter_combinations_of_a_phone_number import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.letterCombinations("789")
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
