from problems.algorithms.problem_0035_search_insert_position import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()


        answer = solution.searchInsert([1,3,5,6], 5)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
