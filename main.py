from problems.algorithms.problem_0303_range_sum_query_immutable import NumArray


class RunProblems:

    @staticmethod
    def run_task():
        solution = NumArray([-2, 0, 3, -5, 2, -1])

        answer = solution.sumRange(0, 2)
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
