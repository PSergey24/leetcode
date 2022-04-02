class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        list_symbols = []
        for element in s:
            if element in list_symbols:
                position = list_symbols.index(element)
                if len(list_symbols) > longest:
                    longest = len(list_symbols)
                list_symbols = list_symbols[position+1:]
                list_symbols.append(element)
            else:
                list_symbols.append(element)
            if len(list_symbols) > longest:
                longest = len(list_symbols)
        return longest
