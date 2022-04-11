from problems.algorithms.problems_to_0200.problem_0190_reverse_bits import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.reverseBits(10100101000001111010011100)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
