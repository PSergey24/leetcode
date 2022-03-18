from problems.algorithms.problem_0045_jump_game_II import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.jump([2,3,1,1,4])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
