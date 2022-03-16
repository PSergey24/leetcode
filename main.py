from problems.algorithms.problem_0027_remove_element import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.removeElement([], 2)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
