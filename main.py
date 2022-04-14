from problems.algorithms.problems_to_0200.problem_0121_best_time_to_buy_and_sell_stock import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.maxProfit([2,7,1,8,3,4])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
