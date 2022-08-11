from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fastPointer = head
        slowPointer = head

        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next

        prev = None
        while slowPointer:
            tmp = slowPointer.next
            slowPointer.next = prev
            prev = slowPointer
            slowPointer = tmp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
