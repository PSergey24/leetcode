from problems.algorithms.problem_0026_remove_duplicates_from_sorted_array import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.removeDuplicates([0,1,1,1,2,3,3])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
