class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num_string = str(x)
            for i in range(0, len(num_string)//2, 1):
                if num_string[i] != num_string[-i-1]:
                    return False
            else:
                return True
