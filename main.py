from problems.algorithms.problems_to_0200.problem_0160_Intersection_of_Two_Linked_Lists import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.getIntersectionNode()
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
