from problems.algorithms.problem_0693_binary_number_with_alternating_bits import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.hasAlternatingBits2(7)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
