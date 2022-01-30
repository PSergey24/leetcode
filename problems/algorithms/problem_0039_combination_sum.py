import copy
import collections
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        current_list = []
        current_list, answers = self.check_all_values(answers, current_list, candidates, target)
        return answers

    def check_all_values(self, answers, current_list, candidates, target):
        for candidate in candidates:
            current_list.append(candidate)
            if self.is_correct_list(current_list, target) is True:
                if self.is_equal(current_list, target) is True and self.is_same_list(answers, current_list) is False:
                    answers.append(copy.copy(current_list))
                    current_list.pop()
                else:
                    current_list, answers = self.check_all_values(answers, current_list, candidates, target)
                    current_list.pop()
            else:
                current_list.pop()
        else:
            return current_list, answers

    @staticmethod
    def is_correct_list(current_list, target):
        return True if sum(current_list) <= target else False

    @staticmethod
    def is_equal(current_list, target):
        return True if sum(current_list) == target else False

    @staticmethod
    def is_same_list(answers, current_list):
        for answer in answers:
            if collections.Counter(answer) == collections.Counter(current_list):
                return True
        else:
            return False

# not my answers:
# https://leetcode.com/problems/combination-sum/discuss/1725562/Python-or-Full-explanation-or-Backtracking-or-Easy-Understanding
# https://www.youtube.com/watch?v=GBKI9VSKdGg