from problems.algorithms.problem_0067_add_binary import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.addBinary("1010", "1011")
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
