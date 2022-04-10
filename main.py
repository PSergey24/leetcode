from problems.algorithms.problems_to_0100.problem_0049_group_anagrams import Solution


class RunProblems:

    @staticmethod
    def run_task():
        solution = Solution()

        answer = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        print(answer)


if __name__ == '__main__':
    run_problems = RunProblems()
    run_problems.run_task()
