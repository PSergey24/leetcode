from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        common_prefix_len = len(first_word)
        for word_num in range(1, len(strs), 1):
            current_word = strs[word_num]

            if len(current_word) == 0:
                return ""

            for n in range(min(len(first_word), len(current_word))):
                if first_word[:n+1] != current_word[:n+1]:
                    common_prefix_len = min(common_prefix_len, n)
                    break
            else:
                common_prefix_len = min(common_prefix_len, len(first_word), len(current_word))

        return strs[0][:common_prefix_len]
