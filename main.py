from problems.algorithms.problem_0091_decode_ways import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.numDecodings("1243")
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
